import pygame

pygame.init()


font20 = pygame.font.Font('freesansbold.ttf', 20)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30


# Prepariamo gli ingredienti

class Giocatore:
    # Chiediamo in input, la posizione iniziale, larghezza, altezza e velocità dell'oggetto
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        # Questo oggetto rettangolo è usato
        self.rettangoloGiocatore = pygame.Rect(posx, posy, width, height)

        self.giocatore = pygame.draw.rect(screen, self.color, self.rettangoloGiocatore)

    # Metodo per mostrare il giocatore a schermo
    def display(self):
        self.giocatore = pygame.draw.rect(screen, self.color, self.rettangoloGiocatore)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        # Blocca il giocatore se cerca d iandare troppo in basso
        if self.posy <= 0:
            self.posy = 0
        # Blocca il giocatore se cerca d iandare troppo in alto
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        # Aggiorna i valori del giocatore
        self.rettangoloGiocatore = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)

    def getRect(self):
        return self.rettangoloGiocatore


class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        # Se la palla colpisce il bordo superiore o inferiore
        # allora cambiamo la direzione sulla y
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    # Cambiamo la direzione della palla quando viene colpita
    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ball


# Definiamo il funzionamento del gioco
def main():
    running = True

    # Definiamo gli ogetti delle classi create sopra
    giocatore1 = Giocatore(20, 0, 10, 100, 10, GREEN)
    giocatore2 = Giocatore(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    listOfGeeks = [giocatore1, giocatore2]

    # Settiamo i parametri iniziali
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)

        # Gestiamo i vari eventi del gioco
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0

        # Controlliamo se ci sono collisioni
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()

        # Aggiorniamo lo stato degli oggetti
        giocatore1.update(geek1YFac)
        giocatore2.update(geek2YFac)
        point = ball.update()

        # -1 -> Giocatore 1 ha segnato
        # +1 -> Giocatore 2 ha segnato
        # 0 -> Nessuno ha segnato
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1

        # Quando viene segnato un punto, resettiamo la palla al centro
        if point:
            ball.reset()

        # Mettiamo a tutti gli effetti gli elementi sullo schermo
        giocatore1.display()
        giocatore2.display()
        ball.display()

        # Mostriamo il testo con i punti dei giocatori
        giocatore1.displayScore("Giocatore_1 : ",
                           geek1Score, 100, 20, WHITE)
        giocatore2.displayScore("Giocatore_2 : ",
                           geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
