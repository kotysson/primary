import sys

import unittest
from pandas import read_csv, isna
from re import search, fullmatch
import zipfile


class DataIntegrityTestCase(unittest.TestCase):
    TEXTS = "publications_txt.zip"
    PUBLICATIONS = "publications_metadata.tsv"
    SUPPLEMENT = "supplement_metadata.tsv"

    def setUp(self):
        self.zip_files_paths = list()
        self.zip_files_names = list()
        self.lengths_lines = list()
        self.lines = list()

        with zipfile.ZipFile(self.TEXTS) as zip_file:
            self.zip_files_paths = list(map(lambda f: f.filename, zip_file.infolist()))

        self.archive = zipfile.ZipFile(self.TEXTS, "r")

        self.zip_files_paths = [zip_file_path for zip_file_path in self.zip_files_paths if zip_file_path != "publications_txt/"]

        for zip_file_path in self.zip_files_paths:
            self.lines.append(self.archive.read(zip_file_path).decode().split("\n"))
            self.lengths_lines.append(len(self.archive.read(zip_file_path).decode().split("\n")))

        self.zip_files_names = [zip_file_name.replace("publications_txt/", "").replace(".txt", "") for zip_file_name in self.zip_files_paths]

        self.publications_metadata = read_csv(self.PUBLICATIONS, sep="\t")
        self.supplement_metadata = read_csv(self.SUPPLEMENT, sep="\t")

        self.publication_parts = [str(integer) for integer in range(1, 25)]
        self.supplement_parts = [str(integer) for integer in range(1, 14)]
        self.query = self.publications_metadata["uid"].value_counts() > 1
        self.query_2 = self.supplement_metadata["uid"].value_counts() > 1
        self.repeating_uid_s_publications_metadata = self.publications_metadata.uid.value_counts()[self.query
        ].index.tolist()
        self.repeating_uid_s_supplement_metadata = self.supplement_metadata.uid.value_counts()[self.query_2
        ].index.tolist()
        self.attributions = ["установлено", "под вопросом", "не установлено", "установлено частично"]
        self.years = list(range(1847, 1867))
        self.types = ["проза", "стихи"]
        self.sections_contents = ["Словесность", "Науки и художества", "Критика и библиография", "Смесь", "Моды",
                                  "От редакции", "Иностранная литература", "Критика", "Библиография",
                                  "Современные заметки", "Литературный ералаш", "Хроника военных событий",
                                  "Словесность, науки и художества", "Устройство быта помещичьих крестьян",
                                  "Современное обозрение", "Свисток. Собрание литературных, журнальных и других заметок"
                                  ]
        self.sections_forms = ["Словесность", "Науки и художества", "Критика и библиография", "Смесь", "Моды",
                               "не указано", "Иностранная литература", "Критика", "Библиография", "Современные заметки",
                               "Литературный ералаш", "Словесность, науки и художества",
                               "Устройство быта помещичьих крестьян", "Современное обозрение",
                               "Свисток. Собрание литературных, журнальных и других заметок"]

        self.numbers = [str(number) for number in range(1, 13)] + ["1–2", "11–12"]
        self.authors = ["Герцен А. И.", "Санд Ж.", "Диккенс Ч.", "Челлини Б.", "неизвестный", "Теккерей В.",
                        "Сильсфильд Ч.", "Диккенс Ч., неизвестный", "Вергилий", "Готорн Н.", "Бульвер-Литтон Э. Д.",
                        "Тютчев Ф. И.", "Бичер-Стоу Г.", "Меллин Г. Г.", "Серре Э.", "Карнович Е. П.", "Милль Д. С.",
                        "Элиот Д.", "Руффини Д.", "Мюльбах Л.", "Шекспир В.", "Гверацци Ф. Д.", "Троллоп Э.",
                        "Тейлор Б.", "Мередит Д.", "Джильберт В."]
        self.translators = ["нет", "Кронеберг А. И.", "Введенский И. И.", "Николаев А. Н., Циммер, неизвестный",
                            "Шершеневич И. Г.", "Бутузов В. В.",
                            "Толль, Борисов, Новосильский, Пашковский, Калистов, Бутузов", "Игнациус", "Ростовцев",
                            "Михайлов М. Л.", "Чернышевский Н. Г.", "Михаловский Д. Л.", "Дружинин А. В.", "Ковалевская"
                            ]

    def test_publications(self):
        """Tests if there are publications of length in lines equal to two and both lines are blank"""
        for index, (p_p, l_l, l) in enumerate(zip(self.zip_files_paths, self.lengths_lines, self.lines)):
            with self.subTest(path_publication=p_p, length_lines=l_l, index=index, line=l):
                self.assertFalse((l_l == 2) and (len([element for element in l if element == ""]) == 2),
                                 f"publication {p_p}: publication is two lines in length and both lines are blank")

    def test_publications_filenames(self):
        """Tests if set of created .txt files is equal to set of possible .txt files listed in
        "publications_metadata.tsv" table and if these sets are of equal lengths"""
        query = self.publications_metadata.filename_txt != "нет"
        filenames_txt = list(self.publications_metadata[query]["filename_txt"])
        self.assertTrue(sorted(filenames_txt) == sorted(self.zip_files_names),
                        f"Set of existing filenames and possible filenames are not equal or of different lengths")

    def test_publications_metadata_na(self):
        """Tests if there are missing values in columns of "publications_metadata.tsv" table"""
        for column in self.publications_metadata.columns[:-1]:
            values = list(self.publications_metadata[column])
            for index, v in enumerate(values):
                with self.subTest(value=v, index=index):
                    self.assertFalse(isna(v), f"row {index}: value {v} in '{column}' column is missing")

    def test_supplement_metadata_na(self):
        """Tests if there are missing values in column of "supplement_metadata.tsv" table"""
        for column in self.supplement_metadata.columns:
            values = list(self.supplement_metadata[column])
            for index, v in enumerate(values):
                with self.subTest(value=v, index=index):
                    self.assertFalse(isna(v), f"row {index}: value {v} in '{column}' column is missing")

    def test_publications_metadata_redundant_spaces(self):
        """Tests if there are redundant spaces in values in column of "publications_metadata.tsv" table"""
        query = self.publications_metadata.dtypes == "object"
        for column in self.publications_metadata.dtypes[query].index:
            values = list(self.publications_metadata[column])
            for index, v in enumerate(values):
                if not isna(v):
                    with self.subTest(value=v, index=index):
                        self.assertFalse(bool(search(pattern=r"\s{2,}", string=v)),
                                         f"row {index}: value {v} in '{column}' column contains redundant spaces")

    def test_supplement_metadata_redundant_spaces(self):
        """Tests if there are redundant spaces in values in column of "supplement_metadata.tsv" table"""
        query = self.supplement_metadata.dtypes == "object"
        for column in self.supplement_metadata.dtypes[query].index:
            values = list(self.supplement_metadata[column])
            for index, v in enumerate(values):
                if not isna(v):
                    with self.subTest(value=v, index=index):
                        self.assertFalse(bool(search(pattern=r"\s{2,}", string=v)),
                                         f"row {index}: value {v} in '{column}' column contains redundant spaces")

    def test_publications_metadata_leading_trailing_spaces(self):
        """Tests if there are leading or trailing spaces in values in column of "publications_metadata.tsv"
        table"""
        query = self.publications_metadata.dtypes == "object"
        for column in self.publications_metadata.dtypes[query].index:
            values = list(self.publications_metadata[column])
            for index, v in enumerate(values):
                if not isna(v):
                    with self.subTest(value=v, index=index):
                        self.assertFalse(bool(search(pattern=r"\s+$|^\s+", string=v)),
                                         f"""row {index}: value {v} in '{column}' column contains trailing or leading
                                         spaces""")

    def test_supplement_metadata_leading_trailing_spaces(self):
        """Tests if there are leading or trailing spaces in values in column of "supplement_metadata.tsv" table"""
        query = self.supplement_metadata.dtypes == "object"
        for column in self.supplement_metadata.dtypes[query].index:
            values = list(self.supplement_metadata[column])
            for index, v in enumerate(values):
                if not isna(v):
                    with self.subTest(value=v, index=index):
                        self.assertFalse(bool(search(pattern=r"\s+$|^\s+", string=v)),
                                         f"""row {index}: value {v} in "{column}" column contains trailing or leading
                                         spaces""")

    def test_uid_part_distinction_publications_metadata(self):
        """Tests "publications_metadata.tsv" if in its rows with same "uid" values there are distinct "part" values"""
        uid_s = list(self.publications_metadata["uid"].unique())
        for u in uid_s:
            with self.subTest(uid=u):
                query = self.publications_metadata.uid == u
                self.assertTrue(
                    len(self.publications_metadata[query].part.unique()) == len(
                        self.publications_metadata[query].part.tolist()), f""""uid" value {u}: there are repeating
                        "part" values for rows with same "uid" values""")

    def test_uid_part_distinction_supplement_metadata(self):
        """Tests "supplement_metadata.tsv" if in its rows with same "uid" values there are distinct "part" values"""
        uid_s = list(self.supplement_metadata["uid"].unique())
        for u in uid_s:
            with self.subTest(uid=u):
                query = self.supplement_metadata.uid == u
                self.assertTrue(
                    len(self.supplement_metadata[query].part.unique()) == len(
                        self.supplement_metadata[query].part.tolist()), f""""uid" value {u}: there are repeating "part"
                        values for rows with same "uid" values""")

    def test_uid_part_numeric_publications_metadata(self):
        """Tests "publications_metadata.tsv" if in its rows with same "uid" values there are only numeric "part"
        values"""
        uid_s = list(self.publications_metadata["uid"].unique())
        for u in uid_s:
            if u in self.repeating_uid_s_publications_metadata:
                with self.subTest(uid=u):
                    query = self.publications_metadata.uid == u
                    parts = self.publications_metadata[query].part.tolist()
                    self.assertTrue(len(parts) == len([part for part in parts if part in self.publication_parts]), f"""
                    "uid" value {u}: there are non-numeric "part" values for rows with same "uid" values""")

    def test_uid_part_numeric_supplement_metadata(self):
        """Tests "supplement_metadata.tsv" if in its rows with same "uid" values there are only numeric "part"
        values"""
        uid_s = list(self.supplement_metadata["uid"].unique())
        for u in uid_s:
            if u in self.repeating_uid_s_supplement_metadata:
                with self.subTest(uid=u):
                    query = self.supplement_metadata.uid == u
                    parts = self.supplement_metadata[query].part.tolist()
                    self.assertTrue(len(parts) == len([part for part in parts if part in self.supplement_parts]), f"""
                    "uid" value {u}: there are non-numeric "part" values for rows with same "uid" values""")

    def test_uid_part_order_publications_metadata(self):
        """Tests "publications_metadata.tsv" if in its rows with same "uid" values there are ordered "part"
        values"""
        uid_s = list(self.publications_metadata["uid"].unique())
        for u in uid_s:
            if u in self.repeating_uid_s_publications_metadata:
                with self.subTest(uid=u):
                    query = self.publications_metadata.uid == u
                    parts = self.publications_metadata[query].part.tolist()
                    self.assertTrue(sorted([int(part) for part in parts]) == [int(part) for part in parts], f"""
                    "uid" value {u}: there are unordered "part" values for rows with same "uid" values""")

    def test_uid_part_order_supplement_metadata(self):
        """Tests "supplement_metadata.tsv" if in its rows with same "uid" values there are ordered "part"
        values"""
        uid_s = list(self.supplement_metadata["uid"].unique())
        for u in uid_s:
            if u in self.repeating_uid_s_supplement_metadata:
                with self.subTest(uid=u):
                    query = self.supplement_metadata.uid == u
                    parts = self.supplement_metadata[query].part.tolist()
                    self.assertTrue(sorted([int(part) for part in parts]) == [int(part) for part in parts], f"""
                    "uid" value {u}: there are unordered "part" values for rows with same "uid" values""")

    def test_only_cyrillic_letters_publications_metadata(self):
        """Tests if values in columns "author", "signature" and "signature_index" in "publications_metadata.tsv" table
        contain only cyrillic characters"""
        for column in ["author", "signature", "signature_index"]:
            values = list(self.publications_metadata[column])
            for index, v in enumerate(values):
                if not bool(fullmatch(pattern=r"[A-Z]\.\s?[A-Z]?\.?", string=v)):
                    with self.subTest(value=v, index=index):
                        self.assertFalse(bool(search(pattern=r"[A-Za-z]", string=v)),
                                         f"row {index+2}: value {v} in '{column}' column contains latin characters")

    def test_only_cyrillic_letters_supplement_metadata(self):
        """Tests if values in columns "author" and "translator" in "supplement_metadata.tsv" table
        contain only cyrillic characters"""
        for column in ["author", "translator"]:
            values = list(self.supplement_metadata[column])
            for index, v in enumerate(values):
                with self.subTest(value=v, index=index):
                    self.assertFalse(bool(search(pattern=r"[A-Za-z]", string=v)),
                                     f"row {index+2}: value {v} in '{column}' column contains latin characters")

    def test_attribution(self):
        """Tests if values in "attribution" column in "publications_metadata.csv" table take only values from specified
        list"""
        attributions = list(self.publications_metadata["attribution"])
        for index, a in enumerate(attributions):
            with self.subTest(attribution=a, index=index):
                self.assertIn(a, self.attributions, f"""row {index+2}: attribution {a} is not equal to one of {
                self.attributions}""")

    def test_type(self):
        """Tests if values in "type" column in "publications_metadata.csv" table take only values from specified
        list"""
        types = list(self.publications_metadata["type"])
        for index, t in enumerate(types):
            with self.subTest(type=t, index=index):
                self.assertIn(t, self.types, f"""row {index+2}: type {t} is not equal to one of {
                self.types}""")

    def test_section_content(self):
        """Tests if values in "section_content" column in "publications_metadata.csv" table take only values from
        specified list"""
        sections_contents = list(self.publications_metadata["section_content"])
        for index, s_c in enumerate(sections_contents):
            with self.subTest(section_content=s_c, index=index):
                self.assertIn(s_c, self.sections_contents, f"""row {index+2}: section_content {s_c} is not equal to one
                of {self.sections_contents}""")

    def test_section_form(self):
        """Tests if values in "section_form" column in "publications_metadata.csv" table take only values from
        specified list"""
        sections_forms = list(self.publications_metadata["section_form"])
        for index, s_f in enumerate(sections_forms):
            with self.subTest(section_form=s_f, index=index):
                self.assertIn(s_f, self.sections_forms, f"""row {index+2}: section_form {s_f} is not equal to one
                of {self.sections_forms}""")

    def test_year_publications_metadata(self):
        """Tests if values in "year" column in "publications_metadata.csv" table take only values from specified list"""
        years = list(self.publications_metadata["year"])
        for index, y in enumerate(years):
            with self.subTest(year=y, index=index):
                self.assertIn(y, self.years, f"""row {index + 2}: year {y} is not equal to one
                        of {self.years}""")

    def test_year_supplement_metadata(self):
        """Tests if values in "year" column in "supplement_metadata.csv" table take only values from specified list"""
        years = list(self.supplement_metadata["year"])
        for index, y in enumerate(years):
            with self.subTest(year=y, index=index):
                self.assertIn(y, self.years, f"""row {index + 2}: year {y} is not equal to one
                        of {self.years}""")

    def test_number_publications_metadata(self):
        """Tests if values in "number" column in "publications_metadata.csv" table take only values from specified
        list"""
        numbers = list(self.publications_metadata["number"])
        for index, n in enumerate(numbers):
            with self.subTest(number=n, index=index):
                self.assertIn(n, self.numbers, f"""row {index + 2}: number {n} is not equal to one
                        of {self.numbers}""")

    def test_number_supplement_metadata(self):
        """Tests if values in "number" column in "supplement_metadata.csv" table take only values from specified list"""
        numbers = list(self.supplement_metadata["number"])
        for index, n in enumerate(numbers):
            with self.subTest(number=n, index=index):
                self.assertIn(n, self.numbers, f"""row {index + 2}: number {n} is not equal to one
                        of {self.numbers}""")

    def test_author(self):
        """Tests if values in "author" column in "supplement_metadata.csv" table take only values from specified list"""
        authors = list(self.supplement_metadata["author"])
        for index, a in enumerate(authors):
            with self.subTest(number=a, index=index):
                self.assertIn(a, self.authors, f"""row {index + 2}: author {a} is not equal to one
                                of {self.authors}""")

    def test_translator(self):
        """Tests if values in "translator" column in "supplement_metadata.csv" table take only values from specified
        list"""
        translators = list(self.supplement_metadata["translator"])
        for index, t in enumerate(translators):
            with self.subTest(translator=t, index=index):
                self.assertIn(t, self.translators, f"""row {index + 2}: translator {t} is not equal to one
                                of {self.translators}""")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        DataIntegrityTestCase.DATA = sys.argv.pop()
    unittest.main()
