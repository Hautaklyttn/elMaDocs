.. include:: <isonum.txt>
.. include:: <isogrk1.txt>

Drehgeber
=========

|

------------

|

Einleitung
----------

Nahezu überall, wo etwas bewegt wird, drehen sich Achsen. Um diese rotatorische Bewegung :navy:`steuern und regeln` zu können, bedarf es Encoder und Motor-Feedback-Systeme. Diese wandeln den Winkel zweier relativ zueinander drehbarer Objekte in ein elektrisches Signal um. Encoder und Motor-Feedback-Systeme unterscheiden sich dabei primär in der Anwendung und sich daraus ergebenden Geräteanforderungen.

:navy:`Encoder` (Lagegeber) werden im Allgemeinen zur Erfassung eines Winkels einer Drehachse verwendet.

:navy:`Motor-Feedback-Systeme` (Motorgeber) sind speziell für den Einsatz in Elektromotoren ausgelegt.

Man kann auch unterscheiden, dass ein Encoder als :navy:`Lastgeber` dient (er misst an der Lastachse) und ein Motor-Feedback-System als :navy:`Motorgeber` (es ist direkt im oder am Elektromotor angebracht).

Allgmein wird bevorzugt der Begriff :navy:`Drehgeber` verwendet, da es sich um allgemeine Darstellungen handelt.

|
|
|

Aufbau
------

Der Sensorkern eines Drehgebers besteht grundsätzlich aus drei Elementen (s.Bild unten). Der :navy:`Sender` bringt Energie in das System ein. Der :navy:`Modulator` verändert die eingebrachte Energie proportional zum mechanischen Winkel |phgr| und dient somit als Maßverkörperung. Der :navy:`Empfänger` wandelt die modulierte physikalische Größe in ein elektrisches Signal. Kombiniert mit Signalverarbeitung, elektrischer und mechanischer Anbindung erhält man einen Drehgeber.

|

.. image:: pics/funcBlocks.png
   :width: 520px

|

Diese abstrakte Betrachtungsweise hinsichtlich Sender-Modulator-Empfänger lässt sich mittels unterschiedlicher sensorischer Prinzipien umsetzen. In Drehgebern finden sich :navy:`optische, magnetische, induktive, kapazitive und resistiv-potenziometrische Sensorkerne`.

Weiterhin kann man nach :navy:`elektromechanischen` und :navy:`mechatronischen` Drehgebern unterscheiden. Bei elektromechanischen Drehgebern sind keine halbleitenden Elemente verbaut, wohl aber bei den mechatronischen. Bei den elektromechanischen Drehgebern stellt der Drehgeber nur den :navy:`Transducer` (dt.: Wandler) dar. Die auswertende Einheit steuert Sender und Empfänger und führt alle Maßnahmen zur Winkelauswertung durch. Bei einem mechatronischen Drehgeber hingegen geschieht dies alles geräteintern. Die aufbereitete Winkelinformation kann mit geringem Aufwand durch die auswertende Einheit verwendet werden.

|
|
|




Messaufgabe
-----------

Die Messaufgabe von Drehgebern besteht darin die :navy:`Winkelstellung` einer rotatorischen Achse zu einem Referenzpunkt zu messen und anzuzeigen. Dabei wird nicht nur die eigentliche Winkelmessung betrachtet, sondern auch die Erfassung abgeleiteter Größen wie die Drehzahl und die Winkelbeschleunigung.

|

.. image:: pics/winkelPhi.png
   :width: 270px

|

Winkel
^^^^^^

Für Winkel verwendet man die Einheiten :navy:`Grad` und :navy:`Radiant`. Dabei hat eine Umdrehung bekanntermaßen 360 Grad (Einheitszeichen °) oder im Bogenmaß, 2 :math:`\pi` Radiant (Einheitszeichen rad). Die beiden Einheiten lassen sich mit dem Umrechnungsfaktor :math:`\rho` einfach in Beziehung setzen:

:math:`\quad \rho = \frac{360°}{2\pi} = \frac{180°}{\pi}`

Ein Grad lässt sich unterteilen in :navy:`Bogen- bzw. Winkelminuten` (1° = 60') oder gar :navy:`Bogen- bzw- Winkelsekunden` (1' = 60''). Manchmal werden auch Milli-Grad (m°; :math:`10^{-3}` °) verwendet. Eine Umdrehung (ein Vollwinkel) hat somit:

1 Umdrehung :math:`\; \widehat{=}` 360° = 21.600' = 1.296.000'' = 360.000m°

Entsprechend ist eine Winkelsekunde annähernd der 1,3 Millionste Teil einer Umdrehung.

|

Winkelgeschwindigkeit
^^^^^^^^^^^^^^^^^^^^^

Neben dem eigentlichen Winkel sind auch daraus ableitbare Größen, wie z.B. die Winkelgeschwindigkeit bzw. :navy:`Drehzahl` für viele Anwendungen relevant.

Die Winkelgeschwindigkeit :math:`\omega` bezeichnet die Änderung des Winkels mit der Zeit:

:math:`\quad \omega = \frac{d\varphi}{dt}`

bzw. bei gleichförmiger Bewegung

:math:`\quad \omega = \frac{\Delta\varphi}{\Delta t}`

Als Einheit für die Winkelgeschwindigkeit verwendet man *rad/s*, seltener *°/s*. In der Technik bezieht man sich oft auf die Anzahl der Umdrehungen pro Zeiteinheit, d.h. die Drehzahl (oder Umdrehungsfrequenz). Hierfür verwendet man die Einheit :navy:`Umdrehungen pro Minute` (*rpm*), 1/min oder :math:`{min}^{-1}` . Formal hat die Winkelgeschwindigkeit und die Drehzahl folgende Beziehung:

:math:`\quad n = \frac{30}{\pi} \cdot \omega = \frac{30}{\pi} \cdot \frac{\Delta\varphi}{\Delta t}`

|

Winkelbeschleunigung
^^^^^^^^^^^^^^^^^^^^

Die Winkelbeschleunigung :math:`\alpha` beschreibt die Änderung  der Winkelgeschwindigkeit :math:`\omega` mit der Zeit. Mathematisch ausgedrückt ergibt sich:

:math:`\quad  \alpha = \frac{d\omega}{dt} = \frac{d²\varphi}{dt²}`

oder bei gleichförmiger Geschwindigkeitsänderung:

:math:`\quad  \alpha = \frac{\Delta\omega}{\Delta t} = \frac{\Delta² \varphi}{\Delta t²}`

Bezogen auf die Drehzahl ergibt sich die folgende Beziehung:

:math:`\quad  \alpha = \frac{\pi}{30} \cdot \frac{\Delta n}{\Delta t}`

Als Einheiten verwendet man *rad/s²*.

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;
   
Messbereich
^^^^^^^^^^^

Bei Drehgebern unterscheidet man primär drei Messbereiche: Teilwinkel, Vollwinkel oder mehrere Umdrehungen. 

Stehen bei Drehgebern eindeutige Winkelwerte über eine mechanische Umdrehung zur Verfügung, spricht man von :navy:`Singleturn-Drehgebern`, bei solchen, die eindeutige Werte über mehrere Umdrehungen ausgeben von :navy:`Multiturn-Drehgebern`.

|

.. image:: pics/turnTypes.png
   :width: 517px

|

Daneben gibt es zwei Sonderfälle zu betrachten:

.. raw:: html

   &nbsp;&bull; &nbsp; <span style="font-size: 16px"><b><font color =#000080>Inkrementalgeber</font></b> zeigen nur eine Winkeländerung (Inkremente) gemäß deren Auflösung an. Diese Funktion steht über eine Umdrehung zur Verfügung.</span><br>
   &nbsp;&bull; &nbsp; <span style="font-size: 16px">Drehgeber mit einer sogenannten <b><font color =#000080>Rundachsfunktion</font></b> (Endloswelle, elektronisches Getriebe) zeigen einen anderen Messbereich an als den,der der verwendeten Sensorik zugrunde liegt. Die Rundachsfunktion erlaubt ganzzahlige und nicht-ganzzahlige Über-und Untersetzungsverhältnisse (s.Bild oben).</span><br>

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;
   
Winkelberechnung
^^^^^^^^^^^^^^^^

Nur wenige Drehgeber erlauben es, einen winkelproportionalen Wert direkt sensorisch zu ermitteln (z.B. resistiv-potentiometrischer Drehgeber). Bei den anderen Prinzipien wird versucht einen in der Mathematik üblichen Weg zu gehen: :navy:`Der Winkel wird auf Basis trigonometrischer Funktionen ermittelt.` Die Sensoren werden so gestaltet, dass bei Drehbewegung sinusförmige Signale entstehen, meist ein :navy:`Sinus- und ein Cosinussignal` (s. Bild unten). Diese Signalpaarung wird auch als Quadratursignale bezeichnet, da sie in Quadratur, d.h. im rechten Winkel stehen (90° Phasenversatz). 

Zur Veranschaulichung kann eine Darstellung am Einheitskreis verwendet werden. Ein Zeiger (Vektor) mit der Länge 1 dreht sich gegen den Uhrzeigersinn. Als Drehachse ist der Koordinatenursprung definiert und als Nullpunkt die Lage des Zeigers auf der Abszisse in positiver Richtung liegend. Die :navy:`y-Komponente des Zeigers repräsentiert den Sinus` und die :navy:`x-Komponente den Cosinus.` Der Winkel :math:`\varphi` wird zwischen dem Vektor und der Abszisse aufgespannt.

|

.. image:: pics/unitCircle.png
   :width: 512px

|

Diese Sinus- und Cosinussignale lassen sich anhand der bekannten trigonometrischen Beziehung

:math:`\quad \tan\varphi = \frac{\sin\varphi}{\cos\varphi}`

wie folgt in einen Winkel umrechnen:

:math:`\quad \varphi = \arctan(\frac{a_{sin}}{a_{cos}})`

( :math:`\varphi` : Errechneter Winkel in [°]; |nbsp| |nbsp| :math:`a_{sin}, a_{cos}` : Momentanwerte der Sinus- und Cosinussignale)