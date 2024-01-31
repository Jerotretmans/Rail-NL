# RailNL

Het Nederlandse spoornetwerk is vaak een bron van frustratie voor menig reizigers. Om dit te verhelpen wordt er met de hulp van verschillende algoritmes geprobeerd een zo optimaal mogelijke dienstregeling te creeëren. Dit wil zeggen; er wordt geprobeerd een dienstregeling te creeëren die over zo veel mogelijk verbindingen rijd, met zo min mogelijk treinen, in een zo kort mogelijke tijd. Om het probleem wat te versimpelen bestaat daarnaast de mogelijkheid om een dienstregeling te creeëren voor de provincies Noord en Zuid Holland. 

## Aan de slag

## Vereisten
Deze codebase is volledig geschreven in Python 3.10.12. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

## Gebruik

Een voorbeeld kan gerund worden door aanroepen van:

```
python main.py <alg>
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

Met het bovenstaande commando wordt het random algoritme aangeroepen.

Na het aanroepen van het commando wordt er in de terminal een aantal vragen gesteld over hoe het algoritme moet worden gerunt:
- Voor regio Holland of Nationaal? (h/nl):
  - Wilt u een dienstregeling creeëren voor regio Holland: vul 'h' in.
  - Wilt u een dienstregeling creeëren voor Nederland: vul 'nl' in.
- Hoeveel trajecten moeten er worden gecreeërd?
  - Wanneer u voor regio Holland heeft gekozen, kies voor 1 - 7 trajecten.
  - Wanneer u voor regio Nederland heeft gekozen, kies voor 1 - 20 trajecten.
  - Zoals uit de experimenten (zie 'Experimenten') blijkt is het optima voor de algoritmes 'greedy', 'hill-climber' & 'simulated annealing' 4 trajecten voor Holland en 10 trajecten voor Nederland.
- Hoe vaak moet het algoritme worden uitgevoerd?
  - Vul een geheel getal in boven de 0
- Wil je een histogram van de data? (y/n):
  - Vul 'y' in voor ja.
  - Vul 'n' in voor nee.


## Structuur
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