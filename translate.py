    ```python
    from googletrans import Translator

    def translate_po_file(input_file, output_file):
      """
      Dịch các cụm từ tiếng Trung từ file .po sang tiếng Việt và lưu vào file .txt.

      Args:
          input_file: Đường dẫn đến file .po.
          output_file: Đường dẫn đến file .txt để lưu kết quả.
      """

      translator = Translator()

      with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        translating = False
        for line in f_in:
          if line.startswith('msgid'):
            translating = True
            original_text = line[7:].strip('"\n')
            f_out.write(f"{original_text}:\n")
          elif line.startswith('msgstr') and translating:
            chinese_text = line[8:].strip('"\n')
            try:
              vietnamese_text = translator.translate(chinese_text, dest='vi').text
              f_out.write(f"{vietnamese_text}\n\n")
            except Exception as e:
              print(f"Lỗi dịch: {e}\nDòng: {line}")
              f_out.write(f"LỖI DỊCH\n\n")
            translating = False

    if __name__ == "__main__":
      input_po_file = "zh-Hans.po"  # Thay tên file .po của bạn
      output_txt_file = "output.txt"  
      translate_po_file(input_po_file, output_txt_file)
    ```
 * Upload file `.po` của bạn lên repository. Nhớ **thay đổi tên file `input.po` trong code  thành tên file `.po` của bạn**. 
