try:
    from .video_processing import track_ball_and_feet
except ImportError:
    from video_processing import track_ball_and_feet
import argparse
import sys
import os

def get_version():
    try:
        from . import __version__
        return __version__
    except ImportError:
        import __init__
        return __init__.__version__

def get_output_names(input_video_path):
    """Génère les noms des fichiers de sortie à partir du nom de la vidéo d'entrée"""
    base_path = os.path.dirname(input_video_path)
    base_name = os.path.splitext(os.path.basename(input_video_path))[0]
    
    output_video = os.path.join(base_path, f"{base_name}_output.mp4")
    output_file = os.path.join(base_path, f"{base_name}_results.txt")
    
    return output_video, output_file

def analyze_ball_touch(input_video_path, display_processing=False, generate_video=False, video_orientation=0):
    """
    Analyse une vidéo de jonglage de football et compte les touches de balle pour chaque pied.
    Génère un rapport détaillé avec le nombre de touches et leur séquence chronologique.
    
    Args:
        input_video_path (str): Chemin d'accès à la vidéo d'entrée
        display_processing (bool, optional): Si True, affiche le traitement en temps réel. Par défaut False (mode silencieux)
        generate_video (bool, optional): Si True, génère une vidéo de sortie avec les annotations. Par défaut False
        video_orientation (int, optional): Orientation de la vidéo en degrés (0, 90, 180, 270). Par défaut 0
    """
    output_video, output_file = get_output_names(input_video_path)
    
    track_ball_and_feet(
        video_source=input_video_path,
        output_video=output_video if generate_video else None,
        output_file=output_file,
        save_output_video=generate_video,
        save_output_file=True,
        silent_mode=not display_processing,
        video_orientation=video_orientation
    )

def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='FootAP - Analyse de touches de balle au football'
    )
    parser.add_argument('-v', '--version', action='store_true', help='Afficher la version')
    
    if args is None:
        args = sys.argv[1:]
    if not ('-v' in args or '--version' in args):
        parser.add_argument('video', help='Chemin vers la vidéo à analyser')
    else:
        parser.add_argument('video', nargs='?', help='Chemin vers la vidéo à analyser')
    
    parser.add_argument('-o', '--output', help='Nom du fichier vidéo de sortie (optionnel)')
    parser.add_argument('-r', '--results', help='Nom du fichier de résultats (optionnel)')
    parser.add_argument('--orientation', type=int, choices=[0, 90, 180, 270], default=0,
                      help='Orientation de la vidéo (0, 90, 180, 270 degrés)')
    parser.add_argument('--display', action='store_true',
                      help='Afficher le traitement en temps réel')
    parser.add_argument('--save-video', action='store_true',
                      help='Générer une vidéo de sortie avec les annotations')
    
    return parser.parse_args(args)

def main(args=None):

    args = parse_args(args)
    
    if args.version:
        print(f"Footap version {get_version()}")
        return
    
   
    analyze_ball_touch(
        input_video_path=args.video,
        display_processing=args.display,
        generate_video=args.save_video,
        video_orientation=args.orientation
    )

if __name__ == "__main__":
    main()