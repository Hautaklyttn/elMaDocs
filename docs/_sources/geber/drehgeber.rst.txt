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

Die Winkelbeschleunigung :math:`\alpha` beschreibt die Änderung  der Winkelgeschwindigkeit :math:`\omega \;` mit der Zeit. Mathematisch ausgedrückt ergibt sich:

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

:under:`Daneben gibt es zwei Sonderfälle zu betrachten:`

:navy:`Inkrementalgeber` zeigen nur eine Winkeländerung (Inkremente) gemäß deren Auflösung an. Diese Funktion steht über eine Umdrehung zur Verfügung.

:navy:`Rundachsfunktion` (Endloswelle, elektronisches Getriebe) - Drehgeber zeigen einen anderen Messbereich an als den, der der verwendeten Sensorik zugrunde liegt. Die Rundachsfunktion erlaubt ganzzahlige und nicht-ganzzahlige Über-und Untersetzungsverhältnisse (s.Bild oben).

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;
   
Winkelberechnung
^^^^^^^^^^^^^^^^

Nur wenige Drehgeber erlauben es, einen winkelproportionalen Wert direkt sensorisch zu ermitteln (z.B. resistiv-potentiometrischer Drehgeber). Bei den anderen Prinzipien wird versucht einen in der Mathematik üblichen Weg zu gehen: :navy:`Der Winkel wird auf :navy:`Basis trigonometrischer Funktionen` ermittelt. Die Sensoren werden so gestaltet, dass bei Drehbewegung sinusförmige Signale entstehen, meist ein :navy:`Sinus- und ein Cosinussignal` (s. Bild unten). Diese Signalpaarung wird auch als Quadratursignale bezeichnet, da sie in Quadratur, d.h. im rechten Winkel stehen (90° Phasenversatz). 

Zur Veranschaulichung kann eine Darstellung am Einheitskreis verwendet werden. Ein Zeiger (Vektor) mit der Länge 1 dreht sich gegen den Uhrzeigersinn. Als Drehachse ist der Koordinatenursprung definiert und als Nullpunkt die Lage des Zeigers auf der Abszisse in positiver Richtung liegend. Die :navy:`y-Komponente des Zeigers repräsentiert den Sinus` und die :navy:`x-Komponente den Cosinus.` Der Winkel :math:`\varphi\;` wird zwischen dem Vektor und der Abszisse aufgespannt.

|

.. image:: pics/unitCircle.png
   :width: 512px

|

Diese Sinus- und Cosinussignale lassen sich anhand der bekannten trigonometrischen Beziehung

:math:`\quad \tan\varphi = \frac{\sin\varphi}{\cos\varphi}`

wie folgt in einen Winkel umrechnen:

:math:`\quad \varphi = \arctan(\frac{a_{sin}}{a_{cos}})`

( :math:`\varphi` : Errechneter Winkel in [°]; |nbsp| |nbsp| :math:`a_{sin}, a_{cos}` : Momentanwerte der Sinus- und Cosinussignale)

Die Gleichung bezieht sich auf eine Sinus-Cosinus-Signalperiode. Hat ein Drehgeber eine solche Signalperiode pro Umdrehung, so ergibt sich direkt die Winkelstellung des Rotors zum Stator. Da in der praktischen Umsetzung die Sinus- und Cosinussignale und somit der sich ergebende Winkel nicht unendlich hoch aufgelöst werden können, Anwendungen aber hohe Auflösungen fordern, :navy:`unterteilt man den Vollwinkel in mehrere Teilwinkel`. Dabei wird jeder Teilwinkel durch eine Signalperiode repräsentiert, man rechnet also mit mehreren Perioden pro Umdrehung (engl.: „periods per revolution", PPR). Dies wird dargestellt durch:

:math:`\quad \varphi_i = \frac{1}{\text{PPR}} \arctan\frac{a_{sin}}{a_{cos}} \quad\quad\quad\quad\quad (1.1)`

( :math:`\varphi_i` : Momentanwert des Winkels der i-ten Periode in [°]; |nbsp| |nbsp| PPR: Anzahl der Periode pro Umdrehung; :math:`\; a_{sin}, a_{cos}` : Momentanwerte der Sinus- und Cosinussignale)

Durch diese Beziehung kann man zwar die Auflösung erhöhen, verliert aber die Aussage über einen absoluten Winkel auf eine Umdrehung. Es ist daher nun sinnvoll :math:`\varphi_{elektr}` und :math:`\varphi_{mech}` einzuführen. :math:`\varphi_{elektr}` bezeichnet :navy:`einen Winkel innerhalb einer elektrischen Periode` und :math:`\varphi_{mech}` jenen auf :navy:`eine mechanische Umdrehung`.

|

.. image:: pics/ppr.png
   :width: 514px

|

Neben der reinen Winkelrechnung kann auf Basis der sinusförmigen Signale auch eine einfache :navy:`Überprüfung der Funktion des Drehgebers` durchgeführt werden. Geben Drehgeber direkt sinusförmige Signale an der elektrischen Schnittstelle aus, kann die bekannte goniometrische Beziehung :math:`\sin²+\cos² = 1` interpretiert werden als:

:math:`a^2_{sin} + a^2_{cos} = \text{const}`

Das Ergebnis wird auch als Vektorlänge bezeichnet. Diese ist in vielen Belangen von hoher Bedeutung. 

Eine weitere Möglichkeit, die sich durch die Verwendung von Sinus- und Cosinussignalen ergibt ist die der Lissajous-Figur. Mit einem Oszilloskop in xy-Darstellung zeichnen die sinusförmigen Signale bei Drehung eine kreisähnliche Form (ein Kreis bei idealen Sinus-Cosinus-Signalen). Der Einheitskreis wird dadurch messtechnisch dargestellt. Auf diese Weise lassen sich verschiedene Qualitätsmerkmale der Quadratursignale abschätzen. Dies ist ein einfach umzusetzendes indikatives Verfahren.

Die eigentliche Winkelrechnung basiert auf Gl. 1.1 (s.oben) wird in diesem Zusammenhang als :navy:`Interpolation` bezeichnet. Interpolatoren können in zwei Dimensionen auf unterschiedliche Weise umgesetzt werden. Zum einen gibt es
verschiedene Verfahren und zum anderen verschiedene Integrationsstufen in der Umsetzung in Hardware und Software. :navy:`Sinus/Cosinus-Digital-Wandler` (engl.:„sine/cosine-to-digital converter"; SDC), wie Interpolatoren auch genannt werden, gibt es als dedizierte ASIC- oder ASSP-Komponenten. Auch kann die Funktion nach Digitalisierung der sinusförmigen Signale durch geeignete Analog-Digital-Wandler mittels Software auf Mikrocontrollern, digitalen Signalprozessoren (DSPs) oder FPGAs implementiert werden. Dabei wird oft der sogenannte CORDIC Algorithmus (engl.: „coordinate rotation digital computer") für die Berechnung der trigonometrischen Funktionen eingesetzt. 

:under:`Bei den Verfahren sollen drei mögliche genannt werden:` 

:navy:`[1]` Der klassische Ansatz ist es :navy:`die Sinus- und Cosinus-Signale gleichzeitig mit linearen Analog-Digital-Wandlern abzutasten` und die digitalen Werte gemäß Gl. 1.1 in einen Winkel umzurechnen. Alternativ kann der Winkelwert aus einer zweidimensionalen Matrix ausgelesen werden, wobei die digitalen Sinus- und Cosinuswerte die Indizes für die Reihen und Spalten darstellen. Vor der Winkelwandlung können die Digitalwerte normiert (z. B. Amplitude) und hinsichtlich Fehlerkomponenten (z. B. Offset) korrigiert werden. 

:navy:`[2]` Ein :navy:`Flash-SDC` ist vergleichbar einem linearen Flash Analog-Digital-Wandler. Bei diesen wird das Eingangssignal mit mehreren Referenzspannungen durch analoge Komparatoren verglichen. Für jeden aufgelösten Schritt wird ein Komparator benötigt. Die Referenzspannungen werden aus einer Spannung durch eine Kaskade von Widerständen gebildet. Beim Flash-SDC werden im Gegensatz dazu zwei Eingangssignale zugeführt und die Widerstandskaskade ist so ausgelegt, dass die Komparatoren Winkelwerte zugeordnet werden. Flash-SDCs sind sehr schnell, der Hardwareaufwand lässt sich allerdings nur für geringe Auflösungen sinnvoll umsetzen. 

:navy:`[3]` Interpolatoren die mit dem :navy:`Nachlaufverfahren` arbeiten, schätzen einen Winkel aus den Signalen ab und führen das Ergebnis auf den Eingang zurück. Dort wird eine Differenz ermittelt, die solange nachgeregelt wird, bis der Fehler minimal wird. Diese Regelung geschieht sehr schnell, insbesondere wenn ein Winkel ermittelt wurde und dieser nur nachgeführt werden muss. 

Die verschiedenen Verfahren unterscheiden sich, u. a. im **Implementierungsaufwand** (Hard- und/oder Software), in der **Schnelligkeit** (somit durch Wandlung eingeführte Latenz), **Auflösung** und **Genauigkeit**.

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;
   
Kodierung
^^^^^^^^^