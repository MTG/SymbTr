#### *SymbTr v2.4.3*
 - Added the second lyrics of four music scores
 - Added Georgi Dzhambazov to contributors

#### *SymbTr v2.4.2*
 - Corrected the lyrics column of several scores
 - Updated the unittest, extras and requirements

#### *SymbTr v2.4.1*
 - Renaming 200+ score filenames
 - Improvements in SymbTr-extras
 - Added key signature validation
 - Corrections in several txt and mu2 scores

#### *SymbTr v2.4*
- Corrected and validated the content of 300+ scores, which had note/duration/phrase/section mistakes.
- Corrected and validated the measure boundaries for the entire collection semi-automatically.
- Added the usul row to the start of each score
- New unittests related to score content: Section name checker, rest name checker, measure boundary checker...
- Regenerated MusicXML files automatically using the first release of [MusicXMLXonverter](https://github.com/burakuyar/MusicXMLConverter).
- Added new scripts in extras: MusicXMLConversion, SymbTr(Meta)DataExtraction, AutomaticOffsetCorrection ...

#### *SymbTr v2.3*
- Corrected and validated the makam, form and usul attributes in symbtr filenames, mu2 file headers, MusicBrainz and Dunya. All these attributes are now consistent with each other. 
- Added unittests to validate scores: score name checker, musicbrainz relation checker, UTF-8 checker for txt and mu2 files, line break checker for txt and mu2 files, mu2 header metadata checker, column name checker for txt and mu2 files, 
- Corrected the usul time signatures in mu2 file headers. 
- Fixed several punctiation mistakes

#### *SymbTr v2.2*
- Added 5 new compositions
- txt and mu2 formats are now encoded in UTF-8.
- Regenerated (and validated) the MusicXML files.
- Fixed errors in the offset column.
- Corrected the implicit and explicit structure markings in the lyrics column of SymbTr-txt files.
- Corrected the contents of several scores (notes, durations etc.).
- Converted "Sus"s to "Es" for consistency (both mean "Rest" in Turkish).
- Added work, makam, usul, form, composer and lyricist metadata to MusicBrainz.
- Renamed many files such that the makam, usul, form and composer slugs in the filename reflects the names in the mu2 file.
- Corrected the metadata of several compositions.
- Added automation scripts to _extras/_ folder

#### *SymbTr v2.1*
- Merged duplicate makam, usul, form and composer names
- If the makam, form, usul and the composers are identical for two distinct compositions they are indexed with numbers in the end of the "lyrics" fields
- Fixed typos in the score names
- Corrected the erroneously associated composers in several compositions 
- Fixed errors in the field separations and the formatting ("--"s)
- Removed special characters in the filenames such as ' and .

#### *SymbTr v2.0*
- __2200 pieces:__ 150 distinct makams, about 100 usuls, 50 forms, 865,000 musical notes, 80 hours nominal playback time.
- __MusicXML and mu2 formats:__ MusicXML is a standard open format for exchanging digital sheet music, which can be read by popular music notation software such as MuseScore, Finale and Sibelius. mu2 is a format, which can be read by Mus2, the microtonal notation software. 
- __Offset column:__ It shows end time of the note in terms of beat unit. If there is an integer value in this column, it means note is at the end of the measure which number is that of the value.
- __Rest marks:__ In *SymbTr v1.0.0* all rest durations were added on the previous note’s duration, in the sense that LNS parameter represents the percentage of notes’ durations. Whereas in v2, the rest marks on the measure boundaries are represented separately, by written '-1' in KomaAE and Koma53 columns.
- __Usul alterations:__ Code 51 in a line represents the point at which passing on a new usul. This kind of records contain time signature of the new usul in Pay (numerator) and Payda (denominator) columns, and the name of it in the Soz1 (syllable) column.
