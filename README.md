*SymbTr*
======
#### Turkish Makam Music Symbolic Data Collection

Given the lack of machine readable symbolic data to perform computational studies of Turkish Makam music, we have put together a collection of machine readable symbolic scores, *SymbTr*, which contains data in text, MusicXML, PDF, MIDI and mu2 formats. This is raw data drawn from reliable sources that consists of musical pieces from Turkish art and folk music. Special care has been taken to select works covering a broad historical time span while being works that are still performed today.

This version also includes the folder symbTr_phraseSegmented. This folder consists of manually segmented *SymbTr* files (~490 pieces) into phrases and also contain some makam-transition labels. 

Please cite the following publication if you use the data collection in your work:
```Karaosmanoğlu, M. K. (2012). A Turkish makam music symbolic database for music information retrieval: SymbTr. Proc. Int. Society for Music Information Retrieval (ISMIR).```

Please also cite the following publication if you use the phrase segmented text scores in your work:
```M. K. Karaosmanoğlu, Barış Bozkurt, Andre Holzapfel and Nilgün Doğrusöz Dişiaçık, "A symbolic dataset of Turkish makam music phrases", Proceedings of FMA, 2014.```

#### What is new in *SymbTr v2.0.0*
1. __2200 pieces:__ 150 distinct makams, about 100 usuls, 50 forms, 865,000 musical notes, 80 hours nominal playback time.
2. __MusicXML and mu2 formats:__ MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software. 
3. __Offset column:__ It shows end time of the note in terms of beat unit. If there is an integer value in this column, it means note is at the end of the measure which number is that of the value.
4. __Rest marks:__ In *SymbTr v1.0.0* all rest durations were added on the previous note’s duration, in the sense that LNS parameter represents the percentage of notes’ durations. Whereas in v2, the rest marks on the measure boundaries are represented separately, by written '-1' in KomaAE and Koma53 columns.
5. __Usul alterations:__ Code 51 in a line represents the point at which passing on a new usul. This kind of records contain time signature of the new usul in Pay (numerator) and Payda (denominator) columns, and the name of it in the Soz1 (syllable) column.

Frequently Asked Questions
--------------

#### Where are the PDFs?

Adding the PDFs to the repository would make it fairly bulky. You can download the PDFs from the CompMusic website (http://compmusic.upf.edu/node/140). You can also follow the link in the corresponding /PDF folder to download the files.
