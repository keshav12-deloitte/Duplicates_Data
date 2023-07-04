# from copydetect import CopyDetector
import copydetect

fp1 = copydetect.CodeFingerprint("/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/pages2/HomeScreen.py", 25, 1)
fp2 = copydetect.CodeFingerprint("/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/pages2/LoginScreen.py", 25, 1)
token_overlap, similarities, slices = copydetect.compare_files( fp1, fp2)
print(token_overlap)

print(similarities[0])

print(similarities[1])
code1, _ = copydetect.utils.highlight_overlap(fp1.raw_code, slices[0], ">>", "<<")
code2, _ = copydetect.utils.highlight_overlap(fp2.raw_code, slices[1], ">>", "<<")
print(code1)
# print(code2)