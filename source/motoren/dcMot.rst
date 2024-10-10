.. include:: <isonum.txt>

Gleichstrommaschine
===================

|

------------

|

Aufbau
------

Jede rotierende elektrische Maschine besteht aus einem feststehenden Teil, dem :navy:`Ständer (Stator)`, und einem rotierenden Teil, dem :navy:`Läufer (Rotor)`. 

   :navy:`Derjenige Teil einer Maschine, in dem Spannungen induziert werden, wird als Anker bezeichnet; bei der Gleichstrommaschine trägt der Läufer die Bezeichnung Anker.`

Meist ist die ganze Maschine zylinderförmig und wird abgeschlossen durch die Lagerschilde an den Stirnseiten des Ständers. Die Lagerschilde halten den Läufer konzentrisch in der Bohrung des Ständers.

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;

Der Ständer
^^^^^^^^^^^

Der Ständer besteht aus dem hohlzylindrischen :navy:`Joch (1)` und den daran befestigten Polen. Da diese Teile keinem magnetischen Wechselfeld unterworfen sind, werden sie aus Guss- oder Walzstahl gefertigt. Die Pole, bestehend aus :navy:`Hauptpolen (2)` und :navy:`Wendepolen (3`), werden innen im Joch angeschraubt; die Hauptpole sind unterteilt in den :navy:`Polkern (5)`, über den die :navy:`Erregerwicklung (6)` gelegt wird, und den :navy:`Polschuh (4)`, der das System zum :navy:`Läufer (7)` hin abschließt (Bild unten).

|

.. image:: pics/dc_staender.png
   :width: 650px

|

Die Erregerwicklungen auf den Hauptpolen sind in Reihe geschaltet und werden mit Gleichstrom gespeist. Bei der eingezeichneten Stromrichtung erzeugen sie einen magnetischen :navy:`Fluss (8) (Hauptfluss)`, der aus dem oberen Hauptpol austritt (Nordpo[), über den Luftspalt in den magnetisch gutleitenden Läufer eintritt und vom Läufer über den zweiten Luftspalt in den unteren Hauptpol (Südpol) fließt. Da magnetische Feldlinien stets auf einem in sich geschlossenen Weg verlaufens dient das Joch als Rückschluss der Feldlinien vom Südpol zum Nordpol, wobei die rechte und linke Jochhälfte je den halben Fluss führen.

Die Wendepole, erregen bei belasteter Maschine ebenfalls einen magnetischen Fluss, der jedoch nicht zur eigentlichen Funktion der Maschine beiträgt.

Das Bild oben zeigt eine zweipolige Maschine (man sprieht auch von Polpaarzahl p = 1); je ein Nord- und ein Südpol ergeben ein Polpaar. In der Praxis werden jedoch nur vier- oder mehrpolige Maschinen (p >= 2) verwendet; ausschließlich Kleinstmotoren werden zweipolig konstruiert. Mehrpolige Gleichstrommaschinen werden deshalb bevorzugt, weil bei ihnen das Material besser ausgenutzt werden kann und weil sie bessere Eigenschaften bei niedrigen Drehzahlen aufweisen als zweipolige Austührungen. Das Bild unten zeigt die Anordnung der Pole und die Flussverteilung bei einer vierpoligen Maschine.

|

.. image:: pics/dc_staender2.png
   :width: 650px

|

Der Läufer
^^^^^^^^^^

Der Läufer (Anker) besteht aus einem zylindrischen Paket von vielen aufeinandergeschichteten und voneinander isolierten Blechen, die auf der Welle befestigt sind. Durch diesen Schichtaufbau — ähnlich der Aufbau weise eines Transformatorkernes — wird verhindert, dass sich im Eisenkern des Läufers ausgeprägte Wirbelströme bilden können. In der Gleichstrommaschine wird zwar kein Wechselfluss erregt, sondern ein zeitlich konstanter Hauptfluss, der sich jedoch für ein betrachtetes Volumenelement des rotierenden Läuferkernes so auswirkt, dass dies Volumenelement einer ständigen Ummagnetisierug
unterliegt.

Infolge dieser Ummagnetisierung entstehen im Läufer neben den Wirbelstrom- auch Hystereseverluste. Um die Hystereseverluste klein zu halten, verwendet man magnetisch weiches Eisen, d. h., Eisen mit schmaler Hystereseschleife (die Fläche der Hystereseschleife ist ein Maß für die Ummagnetisierungsarbeit pro Umlauf). Die Oberfläche des Läufers ist mit Nuten versehen, die in axialer Richtung verlaufen. Sie nehmen die Windungen der Läuferwicklung auf und sind nach außen hin mit einem Verschlusskeil versehen, damit die einzelnen Leiter nicht durch die auftretenden Fliehkräfte aus den Nuten herausgepresst werden. Bei kleinen Maschinen bestehen die Leiter aus lackisoliertem Wicklungsdraht, bei Maschinen großer Leistung aus Rechteckprofil-Kupferbändern mit lackgetränkter Baumwoll- Oder Glasseidenisolation.

Bei sehr großen Maschinen würden die Rechteckleiter in den Nuten derart große radiale Abmessungen aufweisen, dass erhebliche Stromverdrängungserscheinungen zum Luftspalt der Maschine hin auftreten würden. Deshalb Wird der Leiter in mehrere voneinander isolierte Rechteckleiter geringerer Querschnittsfläche aufgeteilt, die innerhalb der Nut jeweils einmal verdrillt sind (Roebelstab), so dass alle Teilleiter im Mittel den gleichen Induktionseinflüssen unterliegen und damit auch mit gleichen Teilströmen belastet sind.

An den beiden Stirnseiten treten die Leiter aus den Nuten heraus, verlaufen bogenförmig weiter und treten in eine andere Nut ein; die Stirnverbindungen sind dabei so ausgelegt, dass an den Stirnseiten des Läufers stets Leiter, die Sich im Bereich eines magnetischen Nordpols befinden, mit solchen Leitern verbunden werden, die an der entsprechenden Stelle unter dem dazugehörenden Südpol verlaufen. Die so gebildeten Drahtwülste der Wicklungsdrähte aller Nuten bilden die Wicklungsköpfe. An einer Seite des Läufers sind diese Wicklungsdrähte an die Lamellen eines :navy:`Stromwenders (Kollektor, Kommutator)` angeschlossen. Dieser ist ein zylindrischer Körper, an dessen Umfang Kupferstreifen in
axialer Richtung nebeneinander angeordnet und voneinander isoliert befestigt sind. Der Stromwender dient in Verbindung mit den Kohlebürsten, die durch Federdruck auf die Lamellen des Stromwenders gepresst werden, der Stromzuführung zum rotierenden Läufer.

Auf der dem Stromwender gegenüberliegenden Läuferseite - bei normaler Bauart das freie Wellenende - ist das Lüfterrad (Ventilator) aufgeschrumpft, das Kühlluft von außen ansaugt und axial durch die Maschine drückt. Die erwärmte Luft tritt kollektorseitig am Lagerschild wieder aus und führt gleichzeitig den Abrieb der Kollektorbürste mit nach außen.

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;

Die Wirkungsweise
-----------------

Grundlagen
^^^^^^^^^^

Aus den Grundlagen über das magnetische Feld ist bekannt, dass auf einen stromdurchflossenen Leiter im Magnetfeld eine Kraft ausgeübt wird. Der Betrag der Kraft F berechnet sich aus 

.. code-block::

       F = l * I * B * sin(a)
	   
	   l   Länge des Leiters im Magnetfeld
	   I   Strom im Leiter
	   B   Induktion des Magnetfeld

mit *a* als Winkel zwischen Strom- und Induktionsrichtung. Verlaufen Strom und Magentfeld senkrecht zueinander (*a* = 90°), vereinfacht es sich zu

.. code-block::

       F = l * I * B

Die Richtung der Kraft F erhält man, wenn man auf kürzestem Wege von der Stromrichtung zur Richtung des Magentfeldes übergeht. Aus dieser vollzogenen Drehung resultiert - bezogen auf den Gang einer Schraube mit Rechtsgewinde - eine Schraubenbewegung die mit der Richtung der Kraft identisch ist.

Das Bild unten zeigt, wie die Kraftrichtung auf anschauliche Weise bestimmt werden kann. Ein stromdurchflossener Leiter (Stromrichtung aus der Zeichenebene heraus) liegt in einem konstanten Magnetfeld der Induktion B. Der Strom baut ein Eigenfeld auf (bei der hier vorgegebenen Stromrichtung verläuft das Eigenfeld gegen den Uhrzeigersinn); beide Felder überlagern sich zu einem resultierenden Feld mit unterschiedlicher Stärke zu beiden Seiten des Leiters. Die Kraft F ist nun so gerichtet, dass sie den Leiter immer in den Bereich der :navy:`Feldschwächung` bewegen will.

|

.. image:: pics/kraftAufLeiter.png
   :width: 552px

|

Erweitern wir diese Erkenntnisse auf eine drehbar gelagerte stromdurchflossene Leiterschleife im Magnetfeld (Bild unten), so ergeben sich Kräfte an den Leiterabschnitten, die in Verbindung mit dem Hebelarm r zu einem Moment führen, das die Anordnung in eine Lage senkrecht zum Magnetfeld ausrichtet.

|

.. image:: pics/drehImMF.png
   :width: 561px

|

In dieser Stellung würde das System verharren. Um eine Drehbewegung aufrechtzuerhalten, ist es deshalb notwendig, dass die Kraftrichtung immer dann geändert wird, wenn die Leiterschleife die zum Magnetfeld senkrechte Ebene (neutrale Zone) durchläuft, :navy:`dies wird durch eine Stromrichtungsumkehr im Leiter erzielt`.

|

Um ein bei konstanter Drehzahl gleichbleibendes Moment zu erzeugen, verwendet man heute bei allen Gleichstrommaschinen die so genannte :navy:`Trommelwicklung`, die aus der Hintereinanderschaltung vieler einzelner Leiterschleifen auf der Mantelfläche eines zylindrischen Läufers (:navy:`Trommelanker`). Die Ankerleiter liegen immer in Nuten, damit nutzt man zwei Vorteile: Die Leiter sind mechanisch gut gegen Fliehkräfte gesichert, und der zwischen Polschuh und Läufer wirksame Luftspalt, der bei vorgegebenem Erregerstrom die Größe der magnetischen Feldstärke beeinflusst, wird klein gehalten.

Jede Leiterschleife ist mit einer Lamelle des Stromwenders verbunden, der in Verbindung mit den Kohlebürsten für die Stromzuführung zum rotierenden Läufer sorgt und so geschaltet ist, dass sich trotz rotierendem Anker eine konstante Stromrichtungsverteilung im Bereich von Nord- und Südpol des Erregerfeldes ergibt.

.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;
   
Der Motorbetrieb
^^^^^^^^^^^^^^^^

Legt man die Erregerwicklunen im Ständer an eine Gleichspannung, so erzeugt der fließende Erregerstrom einen konstanten magnetischen Fluss, der vom Nordpol über Luftspalt und Anker zum Südpol verläuft und über der Ständer wieder zum Nordpol zurückgeführt wird. Beaufschlagt man die Läuferwicklung zusätzlich mit einem Strom,so wird ein Drehmoment auf den Läufer ausgeübt, das diesen in Rotation versetzt. Aufgrund der Drehung der Läuferwicklung im konstanten Magnetfeld wird in der Wicklung eine Spannung U_i induziert, die der amgelegten Ankerspannung entgegengerichtet ist und deren Größe abhängig ist vom konstruktiven Aufbau der Maschine, von der Stärke des Magnetfeldes und von der Umfangsgeschwindigkeit des Ankers, d.h. proportional der Ankerdrehzahl.

Fassen wir die konstruktiv bedingten Werte zu einer *Maschinenkonstanten k1* zusammen, so lässt sich folgender Ersatstromkreis aufstellen:

.. code-block::

       U = U_i + R_a * I
	   
	   U    am Anker angelegte Spannung
	   I    Ankerstrom
	   R_a  ohmscher Widerstand des Ankerkreises
	   U_i  am Anker induzierte Spannung

Die am Anker angelegte Spannung U (Klemmenspannung) teilt sich auf in induzierte Spannung und Spannungsabfall über den ohmschen Widerständen im Ankerkreis.

Soll eine Maschine im Motorbetrieb ein Moment liefern, dann muss sie elektrische Leistung aufnehmen; es muss also bei angelegter Ankerspannung U in die Maschine ein Strom I hineinfließen. Dies ist immer dann der Fall, wenn die Klemmenspannung größer ist als die induzierte Spannung

|nbsp| |nbsp| |nbsp| **Motorbetrieb U > U_i**

Die Höhe des Ankerstromes ist proportional dem geforderten Moment

.. code-block::

       M = F * r
       F = l* I * B
       F ~ I
       M ~ I
	   
Das Moment erzwingt also einen bestimmten Strom, der wiederum resultieren muss aus

|nbsp| |nbsp| |nbsp| **I = (U - U_i) / R_a**
 
Dazu ist bei vorgegebenem Ankerkreiswiderstand eine Spannungsdifferenz notwendig, die sich über die induzierte Spannung U_i durch Änderung der Motordrehzahl einstellt.

|

Bei :navy:`Lastverminderung` liefert ein Gleichstrommotor im Augenblick des Lastwechsels ein höheres Moment als gefordert. Das überschüssige Moment beschleunigt den Läufer, und die Drehzahl der Maschine steigt solange, bis die im Anker induzierte Spannung U_i einen Wert erreicht, der den Ankerstrom so weit vermindert, wie dies für das neue Moment erforderlich ist.

Bei :navy:`Lasterhöhung` gilt Entsprechendes. Das zusätzliche Moment wirkt auf den Läufer bremsend und zwingt ihn zu geringeren Drehzahlen, die dann eine größere Spannungsdifferenz (U - U_i) bewirken und für die Maschine einen höheren Ankerstrom ermöglichen.

|

Da die induzierte Spannung proportional der Drehzahl der Maschine ist (bei Φ = const.), ergibt sich für den Motorbetrieb - bezogen auf die angelegte Klemmenspannung U - ein festgelegtes Drehzahlintervall.

|nbsp| |nbsp| |nbsp| **Motorbetrieb 0 <= n <= n_0**

wobei die :navy:`Leerlaufdrehzahl n_0` dann erreicht wird, wenn die Maschine durch kein Moment belastet wird (weder Lastmoment noch Reibungs- und Eisenverluste). 

|

Der Generatorbetrieb
^^^^^^^^^^^^^^^^^^^^

Die Wendepol- und Kompensationswicklung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. raw:: html

   &nbsp;<br>
   &nbsp;<br>
   &nbsp;<br>
   &nbsp;

Eigenschaften
-------------