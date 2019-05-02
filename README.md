# infortech.github.io

Ce site est conçu avec [Pelican](https://docs.getpelican.com/en/stable/index.html), un générateur de contenu static en Python. 
Dans les grandes lignes, Pelican récupère le contenu du dossier `content` et l'injecte dans les templates du dossier `templates`. 
Le contenu est réparti en catégories correspondant aux différents dossiers présents dans ce répertoire (`seminars`, `projects`, `news` et `thesis`). Chaque catégorie est automatiquement accessible via le menu. Le dossier `pages` référence les pages statiques, également affichées directement dans le menu, à moins qu'une page ne soit explicitement marquée comme `hidden` dans ses méta-données. 

Il est conseillé de rapidement parcourir la documentation de Pelican avant d'effectuer une modification, ou de copier-coller un des fichiers déjà présents et de repartir de ce dernier. 
Notez que toute modification doit avoir lieu dans la branche "sources". Cette dernière est automatiquement compilée à chaque commit, et le résultat placé dans la branche "master", automatiquement affichée par Github pages.