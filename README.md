*SymbTr*
======
#### Turkish Makam Music Symbolic Data Collection

*SymbTr* is a collection machine readable symbolic scores aimed at performing computational studies of Turkish Makam music. SymbTr is currently the biggest machine readable collection of Turkish makam music. The latest version of the SymbTr collection consists of 2200 pieces from 155 makams, 88 usuls, 56 forms, about 865.000 musical notes and 80 hours nominal playback time. 

The scores are selected from reliable sources that consists of musical pieces from Turkish art and folk music. Special care has been taken to select works covering a broad historical time span among the ones which are still performed in the contemporary practice.

SymbTr-scores are provided in text, MusicXML, PDF, MIDI and mu2 formats. MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software.

Please cite the following publication if you use the data collection in your work:
```Kemal Karaosmanoğlu. A Turkish makam music symbolic database for music information retrieval: SymbTr. In Proceedings of 13th International Society for Music Information Retrieval Conference (ISMIR), pages 223–228, 2012.```

Frequently Asked Questions
--------------

#### Where are the PDFs?

Adding the PDFs to the repository would make it fairly bulky. You can download the PDFs from the [SymbTr-pdf repository](https://github.com/MTG/SymbTr-pdf). The repository is also added as submodule to this repository.

#### Is there an easy way to get the section information, especially for vocal sections?
You can use the [symbtrdataextractor package](https://github.com/sertansenturk/symbtrdataextractor) to get the section information.

#### How can I fetch the metadata in MusicBrainz?
[symbtrdataextractor](https://github.com/sertansenturk/symbtrdataextractor) can also be called with MBID input, which will query the desired metadata in MusicBrainz. You can obtain the relevant mbid for each composition from the file [symbTr_mbid.json](https://github.com/MTG/SymbTr/blob/master/symbTr_mbid.json). 

#### I would like to synthesize the scores according to the tuning of a relevant performance. Is it possible?
You can use the [adaptive-tuning](https://github.com/hsercanatli/adaptive-tuning/) package for synthesizing the scores according to the theoretical tuning (Arel-Ezgi-Uzdilek theory) or the tuning performed in a recording.

#### When I open the MusicXML notes in a score editor, the note beams are not connected. How can I fix it?
The beams are not currently connected, because we do not include any beam information in the MusicXML files. Ideally the beams should be connected according to the beat locations of the usul of the piece. We plan to add this in a future release.

Until then, you can select automatic beaming in your score editor. For example, autobeaming can be done in Musescore 2.0 by:
- selecting all notes, and clicking on the Auto option in Note-Beam Properties in Master Palette.

or
- selecting all notes and clicking on Reset Beam Mode under the Layout menu.

#### How do you generate the MusicXML files?
We use [MusicXMLConverter](https://github.com/burakuyar/MusicXMLConverter) package to automatically generate the files using the musical content in the txt files and the metadata stored in the header of the mu2 files. The package is under rapid development and we hope to improve the MusicXML files in the upcoming months.
