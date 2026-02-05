from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import Qt

def imgHandler(file_path, parent_widget, view):
    
    view.setRenderHints(
    QPainter.Antialiasing |
    QPainter.SmoothPixmapTransform
    )

    pixmap = QPixmap(file_path)
    view_width = view.viewport().width()

    scaled = pixmap.scaledToWidth(
     view_width,
     Qt.SmoothTransformation
    )

    scene = QGraphicsScene(view)
    scene.addPixmap(scaled)

    view.setScene(scene)
    view.setSceneRect(scene.itemsBoundingRect())

if __name__ == "__main__":
    pass