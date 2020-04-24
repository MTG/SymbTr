[![DOI](https://zenodo.org/badge/20578855.svg)](https://zenodo.org/badge/latestdoi/20578855) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

*SymbTr*
======
#### Turkish Makam Music Symbolic Data Collection

*SymbTr* is a collection machine readable symbolic scores aimed at performing computational studies of Turkish Makam music. SymbTr is currently the biggest machine readable collection of Turkish makam music. The latest version of the SymbTr collection consists of 2200 pieces from 155 makams, 88 usuls, 56 forms, about 865.000 musical notes and 80 hours nominal playback time. 

The scores are selected from reliable sources that consists of musical pieces from Turkish art and folk music. Special care has been taken to select works covering a broad historical time span among the ones which are still performed in the contemporary practice.

SymbTr-scores are provided in text, MusicXML, PDF, MIDI and mu2 formats. MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software.

Please cite the following publication if you use the data collection in your work:

> M. Kemal Karaosmanoğlu. A Turkish makam music symbolic database for music information retrieval: SymbTr. In Proceedings of 13th International Society for Music Information Retrieval Conference (ISMIR), pages 223–228, 2012.

Frequently Asked Questions
--------------

#### Where are the PDFs?

Adding the PDFs to the repository would make it fairly bulky. You can download the PDFs from the [SymbTr-pdf repository](https://github.com/MTG/SymbTr-pdf). The repository is also added as a submodule to this repository.

#### Are there any tools to do some basic clean-up, conversion etc. on the SymbTr scores?
[SymbTr-extras repository](https://github.com/MTG/SymbTr-extras/tree/2f26c9b88da71f5cd01abd1a24e51f2284d45872) has many such methods. You can request new features in the [issue page](https://github.com/MTG/SymbTr-extras/issues), if it's not yet available.

#### Is there an easy way to get the section information, especially for vocal sections?
You can use the [symbtrdataextractor repository](https://github.com/sertansenturk/symbtrdataextractor) to get the section information.

#### How can I fetch the metadata in MusicBrainz?
[symbtrdataextractor](https://github.com/sertansenturk/symbtrdataextractor) can also be called with MBID input, which will query the desired metadata in MusicBrainz. You can obtain the relevant mbid for each composition from the file [symbTr_mbid.json](https://github.com/MTG/SymbTr/blob/master/symbTr_mbid.json). 

#### Can I synthesize each score according to the tuning of a relevant performance?
You can use the [adaptive-tuning](https://github.com/hsercanatli/adaptive-tuning/) package for synthesizing the scores according to the theoretical tuning (Arel-Ezgi-Uzdilek theory) or the tuning performed in a recording.

#### Is there a way to automatically divide the scores into phrases?
You can follow the instructions in the [makam-symbolic-phrase-segmentation](https://github.com/MTG/makam-symbolic-phrase-segmentation) repository to divide the scores into phrases.

#### I want to do all these operations above without a sweat!
The symbolic analysis modules in [tomato](https://github.com/sertansenturk/tomato) are what you are looking for. Follow the instructions in the [score conversion](https://github.com/sertansenturk/tomato/blob/master/demos/score_conversion_demo.ipynb) and [score analysis](https://github.com/sertansenturk/tomato/blob/master/demos/score_analysis_demo.ipynb) demos for a quick start.

#### When I open the MusicXML notes in a score editor, the note beams are not connected. How can I fix it?
The beams are not currently connected, because we do not include any beam information in the MusicXML files. Ideally the beams should be connected according to the beat locations of the usul of the piece. We plan to add this in a future release.

Until then, you can select automatic beaming in your score editor. For example, autobeaming can be done in Musescore 2.0 by:
- selecting all notes, and clicking on the Auto option in Note-Beam Properties in Master Palette.

or
- selecting all notes and clicking on Reset Beam Mode under the Layout menu.

#### How do you generate the MusicXML files?
We use the [MusicXMLConverter](https://github.com/burakuyar/MusicXMLConverter) package to automatically generate the files using the musical content in the txt files and the metadata stored in the header of the mu2 files. The package is under rapid development and we hope to improve the MusicXML files in the upcoming months.

#### The text is not rendered correctly when the mu2 files are opened in Mus2. How can I fix it?
The mu2 files in this repo has been stored in UTF-8 encoding since [SymbTr v2.2](https://github.com/MTG/SymbTr/releases/tag/v2.2) for compatibility with modern standards. However, Mus2 does not support UTF-8 encoding yet.

Possible solutions are:
- You can open the mu2 files in a modern text reader (such as Sublime text or Visual Studio code) and manually convert the files to either ISO 8859-9 or Windows 1254 encoding.
- You can automate the above step programmatically, e.g. using `iconv` in bash.
- You can use [SymbTr v2.1](https://github.com/MTG/SymbTr/releases/tag/v2.1), however, this version is quite outdated.

<a name="License"></a>License
--------------------
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"/></a><br/> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
