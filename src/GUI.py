import pygame


class GUI:
    def __init__(self, graph, arrX, arrY):
        self.graph = graph
        self.arrX = arrX
        self.arrY = arrY

        def scale(curr_node, min_node, max_node):
            return ((curr_node - min_node) / (max_node - min_node)) * (600 + graph.v_size())

        pygame.init()

        clock = pygame.time.Clock()

        wn_height = 600
        wn_width = 600
        wn = pygame.display.set_mode((wn_width, wn_height))
        pygame.display.set_caption("Draw a Graph")

        state = True
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False

            wn.fill((255, 255, 255))
            my_font = pygame.font.SysFont(None, 25)
            for key in graph.graph:
                pygame.draw.circle(wn, (34, 139, 34), (
                    scale(float(graph.getNode(key).getLocation().x), float(self.arrX[0]),
                          float(self.arrX[len(self.arrX) - 1])),
                    scale(float(graph.getNode(key).getLocation().y), float(self.arrY[0]),
                          float(self.arrY[len(self.arrY) - 1]))), 5)
                text_surface = my_font.render(str(key), True, (0, 0, 139))
                wn.blit(text_surface, (scale(float(graph.getNode(key).getLocation().x), float(self.arrX[0]),
                                             float(self.arrX[len(self.arrX) - 1])),
                                       scale(float(graph.getNode(key).getLocation().y), float(self.arrY[0]),
                                             float(self.arrY[len(self.arrY) - 1]))))

            for key in graph.graph:
                if graph.graph.get(key).Node != None:
                    for index in graph.graph.get(key).Node:
                        srcX = graph.getNode(graph.graph.get(key).Node.get(index).getSrc()).getLocation().x
                        srcY = graph.getNode(graph.graph.get(key).Node.get(index).getSrc()).getLocation().y
                        destX = graph.getNode(graph.graph.get(key).Node.get(index).getDest()).getLocation().x
                        destY = graph.getNode(graph.graph.get(key).Node.get(index).getDest()).getLocation().y
                        pygame.draw.line(wn, (0, 0, 0),
                                         (scale(float(srcX), float(self.arrX[0]), float(self.arrX[len(self.arrX) - 1])),
                                          scale(float(srcY), float(self.arrY[0]),
                                                float(self.arrY[len(self.arrY) - 1]))), (
                                             scale(float(destX), float(self.arrX[0]),
                                                   float(self.arrX[len(self.arrX) - 1])),
                                             scale(float(destY), float(self.arrY[0]),
                                                   float(self.arrY[len(self.arrY) - 1]))))
                else:
                    continue
            pygame.display.update()
            clock.tick(30)

        pygame.quit()