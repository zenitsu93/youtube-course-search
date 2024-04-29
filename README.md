# Recherche de vidéos de cours sur YouTube

Un script qui lit une liste d'intitulés de cours dans un fichier Excel, interroge l'API YouTube Data pour chacun, et écrit les titres et liens des vidéos trouvées dans un second fichier.

L'usage est simple : on a un programme de formation dans un tableur, on veut la ressource vidéo correspondant à chaque chapitre, et on ne veut pas faire cinquante recherches à la main.

## Utilisation

```bash
pip install pandas google-api-python-client openpyxl
```

Obtenez une clé pour l'API YouTube Data depuis la console Google Cloud, renseignez-la dans le script, puis :

```bash
python main.py
```

Le fichier d'entrée doit contenir une colonne d'intitulés ; le fichier de sortie reprend chaque intitulé avec les vidéos associées.

## À savoir

**Le quota est la contrainte principale.** L'API YouTube Data alloue un budget quotidien, et chaque recherche en consomme une part notable — de l'ordre de cent unités sur un quota par défaut de dix mille. Une centaine de recherches suffit donc à l'épuiser. Sur une liste longue, il faut prévoir de traiter par lots sur plusieurs jours, ou demander une augmentation de quota.

**La pertinence n'est pas garantie.** L'API renvoie ce que son moteur juge pertinent pour la chaîne de caractères fournie. Un intitulé de cours ambigu ramènera des résultats hors sujet. Ajouter des mots-clés de contexte au moment de la requête, ou filtrer sur la durée et la chaîne, améliorerait nettement le résultat.
