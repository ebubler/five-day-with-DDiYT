import pygame
from moviepy.editor import VideoFileClip

def play_video(video_path, screen):
    # Загружаем видео с помощью MoviePy
    clip # Масштабируем под ширину окна

    # Конвертируем в массив кадров
    for frame in clip.iter_frames(fps=clip.fps, dtype="uint8"):
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    clip.close()

