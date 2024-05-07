### Описание тестов файла test_integrity.py

Можно запустить командой из терминала из корневой папки дата-сета:

```sh
python3 tests\\/test\_integrity.py
```

1. *test_publications*

Проверяет, есть ли пустые файлы статей

2. *test_publications_filenames*

Проверяет, соответствует ли список созданных файлов статей списку статей из колонки "filename_txt" таблицы "publications_metadata.tsv"

3. *test_publications_metadata_na*

Проверяет, пропущены ли значения в таблице "publications_metadata.tsv"

4. *test_supplement_metadata_na*

Проверяет, пропущены ли значения в таблице "supplement_metadata.tsv"

5. *test_publications_metadata_redundant_spaces*

Проверяет, есть ли в таблице "publications_metadata.tsv" два или более пробелов, идущие подряд

6. *test_supplement_metadata_redundant_spaces*

Проверяет, есть ли в таблице "supplement_metadata.tsv" два или более пробелов, идущие подряд

7. *test_publications_metadata_leading_trailing_spaces*

Проверяет, есть ли в таблице "publications_metadata.tsv" пробелы в начале и в конце значений текстовых колонок

8. *test_supplement_metadata_leading_trailing_spaces*

Проверяет, есть ли в таблице "supplement_metadata.tsv" пробелы в начале и в конце значений текстовых колонок

9. *test_uid_part_distinction_publications_metadata*

Проверяет, являются ли разными значения колонки "part" для рядов таблицы "publications_metadata.tsv" с одинаковыми значениями в колонке "uid"

10. *test_uid_part_distinction_supplement_metadata*

Проверяет, являются ли разными значения колонки "part" для рядов таблицы "supplement_metadata.tsv" с одинаковыми значениями в колонке "uid"

11. *test_uid_part_numeric_publications_metadata*

Проверяет, являются ли числовыми значения колонки "part" для рядов таблицы "publications_metadata.tsv" с одинаковыми значениями в колонке "uid"

12. *test_uid_part_numeric_supplement_metadata*

Проверяет, являются ли числовыми значения колонки "part" для рядов таблицы "supplement_metadata.tsv" с одинаковыми значениями в колонке "uid"

13. *test_uid_part_order_publications_metadata*

Проверяет, являются ли упорядоченными значения колонки "part" для рядов таблицы "publications_metadata.tsv" с одинаковыми значениями в колонке "uid"

14. *test_uid_part_order_supplement_metadata*

Проверяет, являются ли упорядоченными значения колонки "part" для рядов таблицы "supplement_metadata.tsv" с одинаковыми значениями в колонке "uid"

15. *test_only_cyrillic_letters_publications_metadata*

Проверяет, содержатся ли в колонках "author", "signature" и "signature_index" таблицы "publications_metadata.tsv" только буквы кириллического алфавита

16. *test_only_cyrillic_letters_supplement_metadata*

Проверяет, содержатся ли в колонках "author" и "translator" таблицы "supplement_metadata.tsv" только буквы кириллического алфавита

17. *test_attribution*

Проверяет, равны ли значения в колонке "attribution" таблицы "publications_metadata.tsv" одному из возможных значений

18. *test_type*

Проверяет, равны ли значения в колонке "type" таблицы "publications_metadata.tsv" одному из возможных значений

19. *test_section_content*

Проверяет, равны ли значения в колонке "section_content" таблицы "publications_metadata.tsv" одному из возможных значений

20. *test_section_form*

Проверяет, равны ли значения в колонке "section_form" таблицы "publications_metadata.tsv" одному из возможных значений

21. *test_year_publications_metadata*

Проверяет, равны ли значения в колонке "year" таблицы "publications_metadata.tsv" одному из возможных значений

22. *test_year_supplement_metadata*

Проверяет, равны ли значения в колонке "year" таблицы "supplement_metadata.tsv" одному из возможных значений

23. *test_number_publications_metadata*

Проверяет, равны ли значения в колонке "number" таблицы "publications_metadata.tsv" одному из возможных значений

24. *test_number_supplement_metadata*

Проверяет, равны ли значения в колонке "number" таблицы "supplement_metadata.tsv" одному из возможных значений

25. *test_author*

Проверяет, равны ли значения в колонке "author" таблицы "supplement_metadata.tsv" одному из возможных значений

26. *test_translator*

Проверяет, равны ли значения в колонке "translator" таблицы "supplement_metadata.tsv" одному из возможных значений
