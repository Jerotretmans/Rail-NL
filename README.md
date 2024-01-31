# RailNL

Het Nederlandse spoornetwerk is vaak een bron van frustratie voor menig reizigers. Om dit te verhelpen...

## Aan de slag

### Gebruik

Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py alg
```

waar ```alg``` vervangen moet worden door een van de volgende afkortingen:


- rd voor random
- gr voor greedy
- hc voor hill climber
- df voor depth first
- bf voor breadth first
- sa voor simulated annealing

Voorbeeld:

```
python main.py rd
```

Om het random algoritme te runnen.

De terminal zal na het aanroepen van de main een aantal vragen stellen over de details van het runnen van het algoritme. Hieronder valt op welke regio het algoritme moet worden toegepast, hoeveel keer het algoritme uitgevoerd moet worden en of je een histogram van de scores wilt zien na het runnen.


### Structuur
De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de vier benodigde classes voor deze case
  - **/code/visualisation**: bevat de bokeh code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren
- **/docs**: bevat vershillende documenten die van belang zijn geweest tijdens het project

## Experimenten

Naast het main script is er nog een script in de hoofddirectory die gerund kan worden. Dit is experiment.py. Zoals de naam suggereerd is dit het script waarop je een experiment kunt uitvoeren. Er zijn twee experimenten geïmplementeerd (alleen op regio Holland om het even simpel te houden) en ze werken als volgt:

### Experiment 1

Het eerste experiment bepaalt of het handiger is om trajecten bij drukke stations te beginnen of juist bij rustige station, met maar één connectie.

Het eerste experiment kan gerund worden met:

```
python experiment.py exp1
```

Met deze opdracht worden twee situaties met elkaar vergeleken. In de eerste situatie begint het algoritme twee van zijn trajecten op de twee drukste stations (Leiden Centraal en Amsterdam Sloterdijk), en in de tweede situatie begint het op de rustigste stations (Den Helder en Dordrecht).

Het eerste experiment werkt met een random algoritme. De bedoeling is om te kijken of rustige beginstations of drukke beginstations betere resultaten verwerven wanneer al het andere willekeurig is. Het runnen van experiment 1 zet 2 algoritmen in werking van ieder 60 seconden. Aan het einde van het runnen van de algoritmen krijgt de gebruiker achter elkaar twee histogrammen te zien met de verdeling van scores van de twee situaties. Op basis van de histogrammen mag de gebruiker zijn/haar conclusies trekken.

### Experiment 2

Het tweede experiment is er om te bepalen welk aantal trajecten de hoogst mogelijke score wordt bereikt.

Het tweede experiment kan gerund worden met:

```
python experiment.py exp2
```

Na het runnen van deze command komen er 2 prompts, waarin je het algoritme kiest, en waarin je het aantal trajecten kiest.

Met dit experiment kunnen dus per algoritme 7 verschillende situaties worden gemaakt, en die kunnen allemaal met elkaar worden vergeleken. Dit experiment kan op elk algoritme worden toegepast behalve op randalg, omdat daar het aantal trajecten random wordt bepaald. Experiment 2 zet 1 algortime in werking voor 60 seconden die het algoritme blijft runnen met het aangeven aantal trajecten door de gebruiker. Dat resulteert in een lijst met scores en de hoogste score. De scores van de verschillende algoritmen en trajecten kunnen vergeleken worden, en daar kan de gebruiker zijn/haar conclusies trekken.


## Auteurs
- Menno Rooker
- Ron Lakeman
- Jero Tretmans