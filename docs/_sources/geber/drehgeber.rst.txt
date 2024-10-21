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


