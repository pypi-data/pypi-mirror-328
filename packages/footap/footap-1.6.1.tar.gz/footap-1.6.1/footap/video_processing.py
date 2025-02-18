"""Module de traitement vidéo pour la détection de jonglage"""

import cv2
import mediapipe as mp
import numpy as np
from ultralytics import YOLO
from collections import deque
import csv
try:
    from .config import (
        BALL_CLASS_ID,
        CONFIDENCE_THRESHOLD,
        TRACKER_RETRY_FRAMES,
        SMOOTHING_WINDOW,
        YOLO_CHECK_INTERVAL
    )
except ImportError:
    from config import (
        BALL_CLASS_ID,
        CONFIDENCE_THRESHOLD,
        TRACKER_RETRY_FRAMES,
        SMOOTHING_WINDOW,
        YOLO_CHECK_INTERVAL
    )

# Initialisation de MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

class FootTouchCounter:
    """Classe pour compter les touches de balle avec les pieds"""
    
    def __init__(self, min_time=10, touch_threshold=50, fps=30):
        """
        Initialise le compteur de touches.
        
        Args:
            min_time (int): Temps minimum entre deux touches
            touch_threshold (int): Distance seuil pour considérer une touche
            fps (int): Images par seconde de la vidéo
        """
        self.left_foot_touches = 0
        self.right_foot_touches = 0
        self.last_touch_frame = 0
        self.frame_count = 0
        self.min_time = min_time
        self.touch_threshold = touch_threshold
        self.fps = fps
        self.touch_sequence = []  # Liste pour stocker la séquence des touches avec le temps

    def update_touch(self, left_foot, right_foot, ball_x, ball_y):
        """Met à jour le compteur de touches"""
        left_distance = np.linalg.norm(np.array(left_foot) - np.array([ball_x, ball_y]))
        right_distance = np.linalg.norm(np.array(right_foot) - np.array([ball_x, ball_y]))

        if self.frame_count - self.last_touch_frame > self.min_time:
            if left_distance < self.touch_threshold or right_distance < self.touch_threshold:
                # Calculer le temps en secondes depuis le début
                time_seconds = self.frame_count / self.fps
                # Convertir en heures, minutes, secondes et millisecondes
                hours = int(time_seconds // 3600)
                minutes = int((time_seconds % 3600) // 60)
                seconds = int(time_seconds % 60)
                milliseconds = int((time_seconds * 1000) % 1000)
                time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

                if left_distance < right_distance:
                    self.left_foot_touches += 1
                    self.touch_sequence.append({"time": time_str, "foot": "Left"})
                else:
                    self.right_foot_touches += 1
                    self.touch_sequence.append({"time": time_str, "foot": "Right"})
                self.last_touch_frame = self.frame_count

    def get_touches(self):
        """Retourne le nombre de touches pour chaque pied"""
        return self.left_foot_touches, self.right_foot_touches, self.touch_sequence

def rotate_point(x, y, frame_width, frame_height, rotation_angle):
    """Ajuste les coordonnées en fonction de la rotation de la vidéo."""
    if rotation_angle == 90:
        return y, frame_width - x
    elif rotation_angle == 180:
        return frame_width - x, frame_height - y
    elif rotation_angle == 270:
        return frame_height - y, x
    else:
        return x, y

def track_ball_and_feet(video_source, output_video, video_orientation=0, output_file=None, save_output_video=True, save_output_file=True, silent_mode=False):
    """
    Fonction principale pour suivre la balle et les pieds dans une vidéo.
    
    Args:
        video_source (str): Chemin vers la vidéo source
        output_video (str): Chemin pour la vidéo de sortie
        video_orientation (int, optional): Orientation de la vidéo en degrés (0, 90, 180, 270). Par défaut 0
        output_file (str, optional): Fichier de sortie pour les résultats
        save_output_video (bool): Sauvegarder la vidéo de sortie
        save_output_file (bool): Sauvegarder les résultats dans un fichier
        silent_mode (bool): Exécution en mode silencieux sans affichage visuel
    """
    # Initialisation
    model = YOLO("yolo11x.pt")
    tracker = cv2.legacy.TrackerCSRT_create()
    tracking = False
    last_ball_position = None
    tracker_fail_count = 0
    ball_history = deque(maxlen=SMOOTHING_WINDOW)
    frame_count = 0
    foot_touch_counter = FootTouchCounter(min_time=10, touch_threshold=50, fps=30)

    # Ouverture de la vidéo
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir la vidéo.")
        return

    # Configuration de la sortie vidéo
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None
    if save_output_video:
        out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

    # Boucle principale de traitement
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fin de la vidéo.")
            break

        foot_touch_counter.frame_count += 1
        frame_count += 1

        # Rotation de la vidéo si nécessaire
        if video_orientation != 0:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE if video_orientation == 90 else cv2.ROTATE_180 if video_orientation == 180 else cv2.ROTATE_90_COUNTERCLOCKWISE)
            if video_orientation in [90, 270]:
                frame_width, frame_height = frame_height, frame_width

        # Détection de la balle avec YOLO
        if not tracking or tracker_fail_count > TRACKER_RETRY_FRAMES or frame_count % YOLO_CHECK_INTERVAL == 0:
            results = model(frame)
            for result in results[0].boxes.data:
                x1, y1, x2, y2, conf, class_id = result.tolist()
                if int(class_id) == BALL_CLASS_ID and conf > CONFIDENCE_THRESHOLD:
                    ball_x, ball_y = (int((x1 + x2) / 2), int(y2))
                    ball_bbox = (int(x1), int(y1), int(x2 - x1), int(y2 - y1))
                    tracker = cv2.legacy.TrackerCSRT_create()
                    tracker.init(frame, ball_bbox)
                    tracking = True
                    tracker_fail_count = 0
                    last_ball_position = (ball_x, ball_y)
                    break

        # Suivi de la balle
        if tracking:
            success, ball_bbox = tracker.update(frame)
            if success:
                x1, y1, w, h = [int(v) for v in ball_bbox]
                ball_x, ball_y = int(x1 + w / 2), int(y1 + h)
                last_ball_position = (ball_x, ball_y)
                ball_history.append(last_ball_position)
                tracker_fail_count = 0
                cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
                cv2.putText(frame, "Ball", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                tracker_fail_count += 1
                if tracker_fail_count > TRACKER_RETRY_FRAMES:
                    tracking = False

        # Détection des pieds avec MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_pose = pose.process(frame_rgb)

        if results_pose.pose_landmarks:
            landmarks = results_pose.pose_landmarks.landmark
            left_foot = (int(landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x * frame_width),
                         int(landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y * frame_height))
            right_foot = (int(landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x * frame_width),
                          int(landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y * frame_height))

            left_foot = rotate_point(left_foot[0], left_foot[1], frame_width, frame_height, video_orientation)
            right_foot = rotate_point(right_foot[0], right_foot[1], frame_width, frame_height, video_orientation)

            if tracking:
                ball_x, ball_y = rotate_point(ball_x, ball_y, frame_width, frame_height, video_orientation)
                foot_touch_counter.update_touch(left_foot, right_foot, ball_x, ball_y)

        # Affichage des résultats
        left_touches, right_touches, touch_sequence = foot_touch_counter.get_touches()
        
        # Ajouter le texte sur la frame (pour l'affichage et la vidéo de sortie)
        cv2.putText(frame, f"Left Foot Touches: {left_touches}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.putText(frame, f"Right Foot Touches: {right_touches}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        if not silent_mode:
            cv2.imshow("Foot Tracking", frame)

        # Sauvegarde de la vidéo
        if save_output_video and out is not None:
            out.write(frame)

        # Gestion de la sortie
        if not silent_mode and cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Nettoyage des ressources
    cap.release()
    if out is not None:
        out.release()
    if not silent_mode:
        cv2.destroyAllWindows()

    # Sauvegarde des résultats
    if save_output_file and output_file:
        # Fichier texte avec uniquement les totaux
        with open(output_file, 'w') as f:
            f.write(f"Left Foot Touches: {left_touches}\n")
            f.write(f"Right Foot Touches: {right_touches}")

        # Fichier CSV avec les détails temporels
        csv_file = output_file.rsplit('.', 1)[0] + '_details.csv'
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Touch'])  # En-têtes
            for touch in touch_sequence:
                writer.writerow([touch['time'], touch['foot'] + ' Foot'])