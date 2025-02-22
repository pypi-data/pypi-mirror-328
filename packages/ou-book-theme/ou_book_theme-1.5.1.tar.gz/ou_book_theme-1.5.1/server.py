"""Development server."""

import os

from livereload import Server, shell

port = 8000
host = "0.0.0.0"  # noqa: S104

partial_build = shell("jb build docs")
full_build = shell("jb build docs --all")
build_theme = shell("npm run build")

build_theme()
full_build()

server = Server()
server.watch(os.path.join("docs", "**", "*.md"), partial_build)
server.watch(os.path.join("docs", "**", "*.yml"), full_build)
server.watch(os.path.join("docs", "**", "*.png"), full_build)
server.watch(os.path.join("docs", "**", "*.jpg"), full_build)
server.watch(os.path.join("docs", "**", "*.jpeg"), full_build)
server.watch(os.path.join("ou_book_theme", "assets", "**", "*.scss"), build_theme)
server.watch(os.path.join("ou_book_theme", "assets", "**", "*.js"), build_theme)
server.watch(os.path.join("ou_book_theme", "theme", "**", "*.*"), full_build)
server.serve(root=os.path.join("docs", "_build", "html"), port=port, host=host)
