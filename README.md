*SymbTr*
======
#### Turkish Makam Music Symbolic Data Collection

Given the lack of machine readable symbolic data to perform computational studies of Turkish Makam music, we have put together a collection of machine readable symbolic scores called *SymbTr*. Currently, the SymbTr collection consists of 2205 pieces from 155 makams, 84 usuls, 59 forms, about 865.000 musical notes and 80 hours nominal playback time. 

The data is drawn from reliable sources that consists of musical pieces from Turkish art and folk music. Special care has been taken to select works covering a broad historical time span while being works that are still performed today. 

SymbTr-scores are provided in text, MusicXML, PDF, MIDI and mu2 formats. MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software.

Please cite the following publication if you use the data collection in your work:
```Kemal Karaosmanoğlu. A Turkish makam music symbolic database for music information retrieval: SymbTr. In Proceedings of 13th International Society for Music Information Retrieval Conference (ISMIR), pages 223–228, 2012.```

#### What is new in *SymbTr v2.2*
1. Added 5 new compositions
2. txt and mu2 formats are now encoded in UTF-8.
3. Regenerated (and validated) the MusicXML files.
4. Fixed errors in the offset column.
5. Corrected the implicit and explicit structure markings in the lyrics column of SymbTr-txt files.
6. Corrected the contents of several scores (notes, durations etc.).
7. Converted "Sus"s to "Es" for consistency (both mean "Rest" in Turkish).
8. Added work, makam, usul, form, composer and lyricist metadata to MusicBrainz.
9. Renamed many files such that the makam, usul, form and composer slugs in the filename reflects the names in the mu2 file.
10. Corrected the metadata of several compositions.
11. Added automation scripts to _extras/_ folder

#### What is new in *SymbTr v2.1*
1. Merged duplicate makam, usul, form and composer names
2. If the makam, form, usul and the composers are identical for two distinct compositions they are indexed with numbers in the end of the "lyrics" fields
3. Fixed typos in the score names
4. Corrected the erroneously associated composers in several compositions 
5. Fixed errors in the field separations and the formatting ("--"s)
6. Removed special characters in the filenames such as ' and .

#### What is in *SymbTr v2.0*
1. __2200 pieces:__ 150 distinct makams, about 100 usuls, 50 forms, 865,000 musical notes, 80 hours nominal playback time.
2. __MusicXML and mu2 formats:__ MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software. 
3. __Offset column:__ It shows end time of the note in terms of beat unit. If there is an integer value in this column, it means note is at the end of the measure which number is that of the value.
4. __Rest marks:__ In *SymbTr v1.0.0* all rest durations were added on the previous note’s duration, in the sense that LNS parameter represents the percentage of notes’ durations. Whereas in v2, the rest marks on the measure boundaries are represented separately, by written '-1' in KomaAE and Koma53 columns.
5. __Usul alterations:__ Code 51 in a line represents the point at which passing on a new usul. This kind of records contain time signature of the new usul in Pay (numerator) and Payda (denominator) columns, and the name of it in the Soz1 (syllable) column.

Frequently Asked Questions
--------------

#### Where are the PDFs?

Adding the PDFs to the repository would make it fairly bulky. You can download the PDFs from the [SymbTr-pdf repository](https://github.com/MTG/SymbTr-pdf). The repository is also added as submodule to this repository.

#### Is there an easy way to get the section information, especially for vocal sections?
You can use the [symbtrdataextractor package](https://github.com/sertansenturk/symbtrdataextractor) to get the section information.

#### How can I fetch the metadata in MusicBrainz?
[symbtrdataextractor](https://github.com/sertansenturk/symbtrdataextractor) can also be called with MBID input, which will query the desired metadata in MusicBrainz. You can obtain the relevant mbid for each composition from [symbTr_mbid.json](https://github.com/MTG/SymbTr/blob/master/symbTr_mbid.json). 

#### When I open the MusicXML notes in a score editor, the note beams are not connected. How can I fix it?

The beams are not currently connected, because we do not include any beam information in the MusicXML files. Ideally the beams should be connected according to the beat locations of the usul of the piece. We plan to add this in a future release.

Until then, you can select automatic beaming in your score editor. For example, autobeaming can be done in Musescore 2.0 by:
- selecting all notes, and clicking on the Auto option in Note-Beam Properties in Master Palette.

or
- selecting all notes and clicking on Reset Beam Mode under the Layout menu.
