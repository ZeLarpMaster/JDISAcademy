## Fils d'exécution vs Processus

Avant de parler des fils d'exécution et des processus, on doit d'abord parler d'une chose

### GIL

En CPython, la gestion de la mémoire n'est pas faite de manière thread-safe. Il y a donc un Global Interpreter Lock (GIL) qui protège l'accès aux objets Python et empêche plusieurs threads d'exécuter du *bytecode* Python en même temps.

Ce qu'il faut retenir, c'est qu'il n'y a jamais 2 fils d'exécution qui exécutent des *instructions Python* en même temps.

Pour plus d'information sur le GIL: https://wiki.python.org/moin/GlobalInterpreterLock et https://docs.python.org/3/c-api/init.html#thread-state-and-the-global-interpreter-lock

### Fils d'exécution

Les threads en CPython sont tous des threads natifs. Ceci a comme conséquence que ce n'est pas Python qui décide de quel fil d'exécution s'exécute à quel moment. C'est le système d'exploitation qui le décide. À n'importe quel moment, le système d'exploitation peut donc décider d'exécuter un fil sur un coeur et un autre fil sur un autre coeur sans savoir que ça sert à rien puisque le GIL existe. Ces deux fils d'exécution (sur des coeurs différents) vont donc se battre pour obtenir le GIL et exécuter du Python. On peut donc en conclure que n'importe quel programme en Python pur qui tente d'utiliser plusieurs coeurs sera inefficace. Par contre, si un programme en Python pur fait de la concurrence et beaucoup d'E/S, les fils d'exécutions ne passeront pas la majorité de leur temps à tenter d'obtenir le GIL, ils vont plutôt attendre après les E/S.

### Processus

On comprend donc que le GIL ralentit les fils d'exécution, mais qu'en est-il des processus? Le GIL est global par-processus. Donc avec plusieurs processus, on ne se bat plus avec le GIL pour exécuter du code Python. Par contre, on paye immédiatement le coût de démarrer un nouveau processus.

### Asynchrone

Il est aussi possible de faire du code asynchrone en Python. Dans ce cas-ci, on délègue à Python le travail de décider quel tâche s'exécute à quel moment. Cependant, ce travail est fait de manière coopérative, il faut donc que les routines asynchrones donnent explicitement le contrôle lorsqu'elles le veulent. Si on écrit du code synchrone dans une routine asynchrone, on bloque effectivement tout le code asynchrone. L'avantage ici est qu'on se retrouve encore une fois avec un seul fil d'exécution comme le souhaite le GIL.
