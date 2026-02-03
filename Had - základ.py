import pygame

<<<<<<< Updated upstream
# Inicializace Pygame 20
=======
# Inicializace Pygame 2026
>>>>>>> Stashed changes
pygame.init()

# Inicializace hodin pro rizeni snimkovani
hodiny = pygame.time.Clock()

#nastaveni rychlosti
fps=5

#nastaveni pocatecni delky hada
delka=15

# Nastaveni rozmeru okna
sirka_okna = 800
vyska_okna = 600
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption("Had")

# Barvy
barva_hlava = (255,0, 0)  # červena barva
barva_hada = (0, 255, 0)  # zelena barva
barva_pozadi = (0,0, 0)    # cerna barva

# Velikost ctverce
velikost_hada = 10

# Pocatecni pozice hada
pozice= [[sirka_okna // 2,vyska_okna // 2]]

# Pocatecni smer
smer=[1,0]


        

# Hlavni smycka
program_bezi = True
while program_bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            program_bezi = False

    # Ziskani aktualniho stavu klaves
    stav_klaves = pygame.key.get_pressed()

    # Pohyb podle stisknutych klaves
    if stav_klaves[pygame.K_UP]:  # Sipka nahoru
        smer=[0,-1]		    
    if stav_klaves[pygame.K_DOWN]:  # Sipka dolu
        smer=[0,1]
    if stav_klaves[pygame.K_LEFT]:  # Sipka vlevo
        smer=[-1,0]
    if stav_klaves[pygame.K_RIGHT]:  # Sipka vpravo
        smer=[1,0]


    
    # Vyplneni pozadi
    okno.fill(barva_pozadi)

    # Vykresleni hada
    
     
    
    
    for had in pozice:
        pygame.draw.rect(okno, barva_hada, (had[0], had[1], velikost_hada, velikost_hada))

    #posuneme hada
    x=pozice[0][0]+velikost_hada*smer[0]
    y=pozice[0][1]+velikost_hada*smer[1]
  
    pozice.insert(0,[x,y])
    pozice=pozice[:delka]
    
    
    
    # Aktualizace obrazovky
    pygame.display.flip()
  
    # Nastaveni FPS na 60 snimku za sekundu
    hodiny.tick(fps)

# Ukonceni Pygame
pygame.quit()

