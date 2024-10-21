.. include:: <isonum.txt>
.. |br| raw:: html

   <br />

Grundlagen Elektrische Maschinen
================================

|

------------

|

Allgemeine Grundlagen
---------------------

Elektrische Maschinen dienen der **Umformung von Energie**  

.. raw:: html

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &nbsp; <span style="font-size: 16px"><b><font color =#000080>Generatoren</font> erzeugen elektrische Energie</b>  aus mechanischer Energie</span><br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &nbsp; <span style="font-size: 16px"><b><font color =#000080>Motoren</font> erzeugen mechanische Energie</b> aus elektrischer Energie</span><br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &nbsp; <span style="font-size: 16px"><b><font color =#000080>Rotierende Umformer</font> wandeln Frequenz und Spannung</b> elektrischer Energie</span>

|

Trotz aller Vielfalt im konstruktiven Detail, nach dem elektrische Maschinen ausgeführt sein können, Iässt sich ihre Wirkungsweise stets durch Anwendung von nur drei physikalischen Grundgesetzen verstehen und beschreiben: 

* Das :navy:`Induktionsgesetz`, das :navy:`Durchflutungsgesetz` und das :navy:`Kraftwirkungsgesetz`.

|

|

Das magnetische Feld
^^^^^^^^^^^^^^^^^^^^

Je größer die Zahl der nebeneinander liegenden und gleichsinnig vom Strom durchflossenen Leiter ist, desto stärker ist das die Leiter umschließende magnetische Feld. Das Magnetfeld der Spule ist mit dem eines Stabmagneten vergleichbar. Dort wo die Feldlinien die Spule verlassen, bildet sich ein magnetischer Nordpol; dort wo sie in die Spule eindringen, ein Südpol.  

Die Spule stellt somit ein Magnet dar, der sich elektrisch ein- und ausschalten lässt (:navy:`Elektromagnet`). Allerdings ist für die Ausbildung eines starken Magnetfeldes in der Luftspule ein relativ hoher Strom notwendig, der mit einem größeren Querschnitt für den Wickeldraht (Vermeidung einer unzulässigen Erwärmung der Wicklung) verbunden ist.

.. image:: pics/magnFeld.png
   :width: 700px
   
.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;

Die magnetischen Grundgrößen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bei einem Stromfluss durch einen kreisförmigen Leiter, entstehen konzentrische Feldlinien um den Leiter. Fließt ein Strom in den Leiter hinein, verlaufen die Feldlinien im Uhrzeigersinn. Wird die Stromrichtung umgekehrt, ändert sich die Richtung der Feldlinien. Die magnetische Kraft bzw. Stärke des Feldes ist von der Höhe des fließenden Stromes und vom Abstand zum Leiter abhängig:

.. image:: pics/magnFeldstaerke0.png
   :width: 710px

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;

Für die magnetische Feldstärke in einer zylindrischen Luftspule gilt:

.. image:: pics/magnFeldstaerke.png
   :width: 710px

|

|


Die magnetische Wirkung einer Spule lässt sich erheblich steigern, wenn in den Spulenhohlraum ein massives zylindrisches Eisenstück eingeführt wird. Jedes im Spulenkörper befindliche Medium wird von den Feldlinien durchdrungen. Da bei konstanter Feldstärke und Feldlinienzahl die Stoffe Luft und Eisen sehr unterschiedlich Kraftwirkungen verursachen, scheint jeder Stoff einen bestimmten :navy:`magnetischen Widerstand` zu verursachen. Der magnetische Widerstand von Eisen ist geringer als der von Luft oder anders formuliert, die :navy:`magnetische Leitfähigkeit` des Eisens ist höher. Durch die Magnetfeld verstärkende Wirkung des Kernmaterials entsteht ein starker Elektromagnet.  

.. image:: pics/eisenkern.png
   :width: 710px

|

|

   :navy:`Die verstärkende Wirkung beruht darauf, dass bestimmte Materialien ihre Elementarmagnete unter dem Einfluss magnetischer Fremdfelder ausrichten und damit selbst zu einem Magneten werden.` 

Zu ihnen gehören Eisen, Kobalt und Nickel. Sie sind „ferromagnetisch“. Aufgrund dieser Eigenschaft, besitzen sie eine gute magnetische Leitfähigkeit. Die Leitfähigkeit ist allerdings stark von der Stärke des äußeren Magnetfeldes abhängig.

Die Veränderung der magnetischen Leitfähigkeit durch bestimmte Stoffe wird mit Hilfe der :navy:`magnetischen Permeabilität µ` beschrieben. Sie ist vergleichbar mit der Permittivität des Kondensators. Als Maßstab dient auch hier der materiefreie Raum – das Vakuum. Im Vakuum ist die Permeabilität eine konstante Größe. Der absolute Wert dieser Größe wird :navy:`absolute Permeabilität` oder :navy:`magnetische Feldkonstante` :math:`µ_0` genannt.

|

.. image:: pics/perme.png
   :width: 710px

|

|

   :navy:`Eine höhere magnetische Leitfähigkeit führt zu einer Verdichtung der Feldlinien und somit zu einer Konzentration des magnetischen Feldes innerhalb des in die Spule eingebrachten Stoffes. Die höhere Feldliniendichte erzeugt eine größere magnetische Kraft.`

|

Das Produkt aus der magnetischer Feldstärke und der Permeabiltät macht eine Aussage über die Feldliniendichte. Sie wird :navy:`magnetische Flussdichte B` oder :navy:`magnetische Induktion` genannt.

|

.. image:: pics/magnFlussd.png
   :width: 710px

|

|

   :navy:`Nur die magnetische Flussdichte B kann etwas über die Stärke eines Magnetfeldes aussagen, denn nur sie berücksichtigt die Permeabilität und somit die magnetische Leitfähigkeit eines Materials bzw. der Luft.`

|

Wie bei einem elektrischen Leiter, dessen Leitwert vom Material, der Leiterlänge und dem Querschnitt abhängt, lässt sich auch für den magnetischen Kreis ein magnetischer Leitwert berechnen. Besonders einfach wird die Berechnung des Leitwertes, wenn es sich um ein homogenes und auf einen definierten räumlichen Bereich beschränktes magnetisches Feld handelt. Fließt ein Strom durch einen Spulendraht, der lediglich einmal (N = 1) um einen geschlossenen Eisenkern gewickelt wurde, so verlaufen die meisten Feldlinien im räumlich begrenzten Kernmaterial.

|

.. image:: pics/leitwert.png
   :width: 450px

|

|

Für die im Kern verlaufenden Feldlinien lässt sich die mittlere Feldlinienlänge lm über die Kernabmessungen bestimmen. Die Querschnittsfläche A ergibt sich aus dem Produkt der Kantenlängen und die materialspezifische Permeabilität kann mit Hilfe der Magnetisierungskennlinie des Herstellers für eine bestimmte Feldstärke H über die Gleichung der magnetischen Flussdichte B berechnet werden. Die Abmessungen des Eisenkernes beeinflussen somit unmittelbar den magnetischen Leitwert. Dieser steigt (in Analogie zum Leitwert eines elektrischen Leiters) mit höherer magnetischer Leitfähigkeit des Materials, bei Abnahme der mittleren Feldlinienlänge und bei Vergößerung des Querschnittes.

|

.. image:: pics/magnLeitwert.png
   :width: 710px

|

|

In Abhängigkeit der magnetischen Flussdichte B und dem magnetischen Widerstand :math:`R_m` bzw. Leitwert Λ, bildet sich innerhalb des in der Spule befindlichen Werkstoffes, ein :navy:`magnetischer Fluss Φ` (Phi) aus. Dieser ist vergleichbar mit dem elektrischen Strom durch einen Leiterwiderstand. Der magnetische Fluss repräsentiert die Gesamtzahl aller auftretenden Feldlinien und somit die Höhe des „magnetischen Stromes“. Ein größerer Querschnitt A des Werkstoffes bzw. des Hohlraumes senkt den magnetischen Widerstand :math:`R_m` und führt zu einem höheren magnetischen Fluss. Wird die magnetische Flussdichte B erhöht (größerer Strom, höhere Windungszahl, Kernmaterial mit höherer Permeabilität), so führt auch das zu einem proportionalen Anstieg des magnetischen Flusses Φ.

|

.. image:: pics/magnFluss.png
   :width: 710px

|

|

Im Bild unten wird die Analogie zwischen dem elektrischen Stromkreis und dem magnetischen Kreis mit Hilfe der dazugehörigen Größen verdeutlicht.

Die Spannungsquelle U des elektrischen Stromkreises lässt sich aus in Reihe geschalteten Primärzellen (:math:`U_0`) zusammensetzen. Im magnetischen Kreis ist die magnetische Durchflutung Θ die „Spannungsquelle“. Die Durchflutung steigt mit der Größe des Stromes und der Zahl der Windungen.

|

.. image:: pics/elMagnKreis.png
   :width: 690px

|

Nachfolgend sind die Zusammenhänge der beiden Kreise in tabellarischer Form zusammengefasst.

|

.. image:: pics/verglElMagn.png
   :width: 710px


|

------------

|

Drehstrom oder Gleichstrom?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ein Rückblick auf die Entwicklung zeigt den Weg. War früher ein Antrieb mit fester Drehzahl über einen Drehstromasynchronmotor mit Verteilung der mechanischen Leistung über Transmissionen üblich, ging der Trend Ende der 90er verstärkt zum angepassten Einzelmotorenantrieb (Module). Der Einsatz der Halbleitertechnik begünstigte diese Entwicklung.

Zunächst fanden :navy:`Halbleitergeräte als netzgeführte Stromrichter oder Steller im Gleichstrombereich` Eingang in die Technik der drehzahlvariablen Antriebe. Damit kann die Ankerspannung eines Gleichstrommotors und damit die Drehzahl in weiten Bereichen kontinuierlich und nahezu verlustfrei verstellt werden. Die Verstellung kann erfolgen; verschleißbehaftete Stellwiderstände usw. entfallen. Über den Ankerstrom kann damit auch gleichzeitig das Drehmoment geregelt begrenzt werden. Auf diesem Wege lassen sich Antriebe aufbauen, die sanft und ruckfrei anlaufen, die gewünschte vorgewählto Drehzahl lastunabhängig halten und mit einer hohen Dynamik arbeiten.  

Der Gleichstrommotor benötigt einen mechanischen Stromwenderapparat. Hierin begründet liegt — trotz stark verbesserter Bürstenstandzeiten von bis zu 20.000 Betriebsstunden — wegen des Verschleißes an Stromwender und Bürsten ein gewisser Wartungsaufwand. Überdies erfordert der Stromwender Rücksichtnahme manchen Einsatzfällen, z. B. bei aggressiver Atmosphäre, Rüttelkräften, hohen Drehzahlen über :math:`4.500 \text{min}^{-l}` oder bei Stillstandsbelastung.  

Bei solchen Einsatzfällen hat der :navy:`Drehstrommotor mit Kurzschlussläufer` Vorteile, da bei ihm die elektrische Leistung verschleißfrei über das Drehfeld vom Ständer auf den Läufer übertragen wird. Die einfach aufgebaute Käfigwicklung im Läufer lässt hohe Drehzahlen zu; die vollständige Kapselung ermöglicht den Betrieb in fast jeder Umgebung. Der Einsatz der Frequenzumrichter zur Speisung der Drehfeldmaschinen brachte so eine Umorientierung der elektrischen Antriebstechnik.

|

.. image:: pics/dcVsAsync.png
   :width: 620px

|

War der Drehstrommotor bislang an die vom Netz vorgegebene feste synchrone Drehzahl gebunden, so ermöglichte es der :navy:`Frequenzumrichter` aus jedem Drehstrom-Normmotor
einen drehzahlvariablen Antrieb zu machen. Frequenz und Spannung des Wechselstrom- oder Drehstromnetzes werden vom Frequenzumrichter so variiert, dass der Motor in weiten
Stellbereichen drehzahlvariabel betrieben werden kann. Die Elektronik erlaubt dabei eine gute Anpassung an die Charakteristiken der Arbeits- oder Kraftmaschinen. Die Einführung der
Digitaltechnik brachte auch der Regelverfahren, die sogar bessere Dynamiken als die Gleichstromantriebe erreichen. Hier zeichnen Sich heute im Besonderen Servoantriebe, bestehend aus Servo-Umrichter und trägheitsmomentarmen Servomotoren, aus.

|

Was wird wo eingesetzt?
^^^^^^^^^^^^^^^^^^^^^^^

Die fortschreitende Automatisierung verlangt Antriebe mit großem Drehzahlssteuerbereich und guten Regeleigenschaften. Obwohl im Allgemeinen keine Gleichstromnetze zur Verfügung stehen, werden vorwiegend :navy:`Gleichstrom-Nebenschlussmotoren und Doppelschlussmotoren` eingesetzt, da sie für die vorher genannten Forderungen besonders gut geeignet sind und sich eine Einspeisung über steuerbare Stromrichter preiswert realisieren lässt.

Für den Antrieb elektrisch betriebener Fahrzeuge verwendet man :navy:`Gleichstrom- und Einphasen-Reihenschlussmotoren`, z. B. in Straßenbahnen (meist Gleichstrom) und E-Lokomotiven (meist Wechselstrom, neuerdings Drehstromasynchronmotoren). Einphasen-Reihenschlussmotoren trifft man auch in Elektrowerkzeugen und Haushaltsmaschinen an; ebenfalls den Einphasen-Asynchronmotor (Waschmaschine). :navy:`Einphasen-Synchronnmotoren` dienen aufgrund ihrer konstanten Drehzahl als Antrieb für Tonband und Plattenspieler und als Kleinstmotoren in Programmschaltwerken.

Der :navy:`Drehstrom-Asynchronmotor` ist der am weitesten verbreitete Elektromotor. Dank seines einfachen und robusten Aufbaus ist er unempfindlich gegen Überbelastung und äußerst wartungsarm, sodass bei einer Antriebsplanung zuerst die Möglichkeit des Einsatzes dieser Maschinen geprüft wird. Deshalb ist sein Einsatzgebiet auch so groß, dass man kaum spezielle Bereiche angeben kann.

Der :navy:`Drehstromsynchronmotor` wird gern in der Industrie als großer, langsam laufender Elektromotor mm Antrieb von Kolbenverdichtern eingesetzt. Zudem kann er — aufgrund seines kapazitiven Betriebsverhaltens — den induktiven Anteil des Laststromes großer Verbraucher kompensieren.

Mit den bisher genannten elektrischen Maschinen wird das Gebiet der elektrischen Antriebstechnik abgedeckt. Die Erzeugung elektrischer Energie ist heute das Spezialgebiet der :navy:`Drehstromsynchrongeneratoren`. (Eine Ausnahme stellt nur der Gleichstrom-Doppelschlussgenerator, der in Einzelfällen noch zur Erzeugung von Gleichspannungen eingesetzt wird.) In den Dampf- und Wasserkraftwerken arbeiten riesige Synchronmaschinen mit 200 MW Leistung in Standardausführung bis hinauf zu Höchstleistungsmaschinen mit 1311 MW.

|

------------

|

Merksätze
^^^^^^^^^

	:navy:`Ein permanenterregter Motor wird über Permanentmagnete erregt, ein fremderregter Motor wird über eine separat anzulegende Spannungsquelle erregt. Beide haben prinzipiell die Charakteristik eines Nebenschlussmotors, da die Erregung vom Ankerstrom unabhängig ist.`
	
	|br|

	:navy:`Prinzipiell ist das Drehmoment proportional dem Produkt aus magnetischem Fluss und Ankerstrom. Wenn allerdings, wie beim Reihenschluss- oder Asynchronmotor der Fluss lastabhängig ist, schummelt sich da der Strom noch einmal in die Formel rein: Für DIESE Motoren gilt dann M = k * I²`


