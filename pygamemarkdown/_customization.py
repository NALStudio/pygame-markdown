import pygame


def set_font_sizes(self, h1=20, h2=18, h3=15, normal=15):
    self.font_header_size = h1
    self.font_header2_size = h2
    self.font_header3_size = h3
    self.font_normal_size = normal
    self.reload_fonts()


def set_font(self, font='Arial'):
    self.font = font
    self.reload_fonts()


def reload_fonts(self):
    self.font_header = pygame.font.SysFont(self.font, self.font_header_size, bold=True)
    self.font_header2 = pygame.font.SysFont(self.font, self.font_header2_size, bold=True)
    self.font_header3 = pygame.font.SysFont(self.font, self.font_header3_size, bold=True)
    self.font_text = pygame.font.SysFont(self.font, self.font_normal_size)


def set_line_gaps(self, gap_line=5, gap_paragraph=30):
    self.gap_line = gap_line
    self.gap_paragraph = gap_paragraph
