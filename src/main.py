import argparse
from detector import PersonDetector
from video_processor import VideoProcessor

def main():
    parser = argparse.ArgumentParser(description="Detecção de Pessoas")
    parser.add_argument('--video_path', type=str, required=True, help="Caminho para o vídeo de entrada")
    parser.add_argument('--limiar_pessoas', type=int, required=True, help="Número mínimo de pessoas para gerar um alerta")
    parser.add_argument('--output_dir', type=str, default='./output_results', help="Pasta para salvar os resultados")
    args = parser.parse_args()

    detector = PersonDetector()
    processor = VideoProcessor(
        input_video_path=args.video_path,
        output_dir=args.output_dir,
        alert_threshold=args.limiar_pessoas,
        detector=detector
    )
    processor.process_video()

if __name__ == "__main__":
    main()