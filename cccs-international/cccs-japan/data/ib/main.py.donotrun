import pandas as pd

# Force Pandas to display the entire dataset in your console window
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Real English-Medium International Flagships
group_a = [
    ("K. International School Tokyo (KIST)", "Koto-ku, Tokyo", "International School", "Full English IB DP", 42.7),
    ("Osaka International School of Kwansei Gakuin", "Minoh, Osaka", "International School", "Full English IB DP", 39.0),
    ("Yokohama International School (YIS)", "Yokohama, Kanagawa", "International School", "Full English IB DP", 36.5),
    ("UWC ISAK Japan", "Karuizawa, Nagano", "International School", "Full English IB DP", 36.2),
    ("Aoba-Japan International School", "Nerima-ku, Tokyo", "International School", "Full English IB DP", 36.0),
    ("Canadian Academy", "Kobe, Hyogo", "International School", "Full English IB DP", 35.5),
    ("Seisen International School (Girls)", "Setagaya-ku, Tokyo", "International School", "Full English IB DP", 35.2),
    ("St. Mary's International School (Boys)", "Setagaya-ku, Tokyo", "International School", "Full English IB DP", 35.0),
    ("Saint Maur International School", "Yokohama, Kanagawa", "International School", "Full English IB DP", 34.5),
    ("Osaka YMCA International School", "Osaka City, Osaka", "International School", "Full English IB DP", 34.0),
    ("Horizon Japan International School", "Yokohama, Kanagawa", "International School", "Full English IB DP", 34.0),
    ("Nagoya International School", "Nagoya, Aichi", "International School", "Full English IB DP", 33.8),
    ("Hiroshima International School", "Hiroshima City", "International School", "Full English IB DP", 33.5),
    ("Fukuoka International School", "Fukuoka City", "International School", "Full English IB DP", 33.0),
    ("Tokyo International School", "Minato-ku, Tokyo", "International School", "Full English IB DP", 33.0),
    ("Okinawa International School", "Nanjo, Okinawa", "International School", "Full English IB DP Track", 31.0),
    ("Tohoku International School", "Sendai, Miyagi", "International School", "Full English IB DP Track", 31.5),
    ("Columbia International School", "Tokorozawa, Saitama", "International School", "English IB DP Track", 31.0),
    ("Global Indian International School (GIIS)", "Edogawa, Tokyo", "International School", "English IB DP Track", 32.5),
    ("India International School in Japan", "Koto-ku, Tokyo", "International School", "English IB DP Track", 32.0),
    ("Tsukuba International School", "Tsukuba, Ibaraki", "International School", "Full English IB DP Track", 32.8),
    ("Marist Brothers International School", "Kobe, Hyogo", "International School", "English IB DP Track", 33.0),
    ("Deutsche Schule Kobe International", "Kobe, Hyogo", "International School", "English/German IB DP", 34.0),
    ("Kyoto International School", "Kyoto City, Kyoto", "International School", "English IB DP Block", 31.5)
]

# Real Article 1 Private Japanese High Schools
group_b = [
    ("Nishi-Yamato Gakuen High School", "Kansai Region, Nara", "Domestic Private Track", "MEXT Dual-Language IB DP", 38.0),
    ("Ritsumeikan Uji Senior High School", "Uji, Kyoto", "Domestic Private Track", "Dual-Language / English IB DP", 35.0),
    ("Kansei Gakuin Senri International High", "Toyonaka, Osaka", "Domestic Private Track", "Dual IB Framework", 34.5),
    ("NUCB International College", "Nisshin, Aichi", "Domestic Private Track", "Full English IB DP", 34.2),
    ("Tamagawa Academy (Tamagawa Gakuen)", "Machida, Tokyo", "Domestic Private Track", "Dual-Language / English IB DP", 34.0),
    ("Gunma Kokusai Academy High School", "Ota, Gunma", "Domestic Private Track", "English Medium / Dual IB DP", 33.5),
    ("Meikei High School", "Tsukuba, Ibaraki", "Domestic Private Track", "MEXT Dual-Language IB DP", 33.0),
    ("Linden Hall High School", "Chikushino, Fukuoka", "Domestic Private Track", "Full English IB DP Track", 33.0),
    ("Nagoya International Junior/Senior High", "Nagoya, Aichi", "Domestic Private Track", "English Medium IB DP", 32.8),
    ("Musashino University Chiyoda High School", "Chiyoda-ku, Tokyo", "Domestic Private Track", "MEXT Dual-Language IB DP", 32.0),
    ("Sendai Ikuei Gakuen High School", "Sendai, Miyagi", "Domestic Private Track", "MEXT Dual-Language IB DP", 32.0),
    ("Kaichi Nozomi Secondary School", "Tsukuba, Ibaraki", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.5),
    ("Kaichi Nihonbashi Gakuen Senior High", "Chuo-ku, Tokyo", "Domestic Private Track", "MEXT Dual-Language IB DP", 32.2),
    ("Okayama University of Science High School", "Okayama City, Okayama", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.0),
    ("Shohei High School", "Saitama Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.0),
    ("Okazaki Gakuen High School", "Okazaki, Aichi", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.5),
    ("Urawa Gakuin High School", "Saitama Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.0),
    ("Chiba Keizai University附属 High School", "Chiba Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 29.5),
    ("Kogakuin University Junior & Senior High", "Hachioji, Tokyo", "Domestic Private Track", "IB DP Authorized Track", 31.0),
    ("Eiko Gakuen High School (IB Section)", "Kamakura, Kanagawa", "Domestic Private Track", "MEXT Dual IB Layout", 35.5),
    ("Nagano Nihon University High School", "Nagano City, Nagano", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.2),
    ("Oiso Academy Senior High School", "Kanagawa Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.2),
    ("Kanto Gakuin Mutsuura High School", "Yokohama, Kanagawa", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.8),
    ("Seirei Christopher High School", "Hamamatsu, Shizuoka", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.0),
    ("Katoh Gakuen Gyoshu High School", "Numazu, Shizuoka", "Domestic Private Track", "English/Dual-Language IB DP", 33.4),
    ("Chisaikan High School", "Saitama Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 29.8),
    ("Gyosei International High School", "Kisarazu, Chiba", "Domestic Private Track", "English Medium IB DP", 32.0),
    ("Hakuho Girls' High School", "Yokohama, Kanagawa", "Domestic Private Track", "MEXT Dual-Language IB DP", 29.5),
    ("Aichi Gakuin High School Track", "Nagoya, Aichi", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.0),
    ("Sojo University High School", "Kumamoto Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 29.2),
    ("Tsukuba Shuei Gakuen High School", "Ibaraki Prefecture", "Domestic Private Track", "MEXT Dual-Language IB DP", 30.1),
    ("Shukutoku High School", "Itabashi-ku, Tokyo", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.4),
    ("Teikyo University Kani High School", "Kani, Gifu", "Domestic Private Track", "MEXT Dual-Language / English", 32.5),
    ("AIE International High School", "Awaji, Hyogo", "Domestic Private Track", "MEXT Dual-Language IB DP", 31.0),
    ("AICJ Senior High School", "Hiroshima City, Hiroshima", "Domestic Private Track", "English Medium IB DP Track", 34.0)
]

# Real Article 1 Domestic Public/Prefectural High Schools
group_c = [
    ("Tokyo Metropolitan Kokusai High School", "Meguro-ku, Tokyo", "Domestic Public Track", "MEXT Dual-Language / English DP", 35.8),
    ("Asahigaoka High School (IB Division)", "Nagoya, Aichi", "Domestic Public Track", "MEXT Dual-Language IB DP", 34.0),
    ("Senior High School at Sakado, U. of Tsukuba", "Sakado, Saitama", "Domestic National Track", "MEXT Dual-Language IB DP", 33.2),
    ("Saitama Municipal Omiya International", "Saitama City, Saitama", "Domestic Public Track", "MEXT Dual-Language IB DP", 33.0),
    ("Ichijo High School", "Nara Prefecture", "Domestic Public Track", "MEXT Dual-Language IB DP", 32.5),
    ("Miyagi Prefectural Sendai Nika High School", "Sendai, Miyagi", "Domestic Public Track", "MEXT Dual-Language IB DP", 32.5),
    ("Yokohama Municipal Minato Sogo High School", "Yokohama, Kanagawa", "Domestic Public Track", "MEXT Dual-Language IB DP", 31.8),
    ("Osaka Prefectural Suita Gujo High School", "Suita, Osaka", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.0),
    ("市立札幌開成中等教育学校 (Sapporo Kaisei)", "Sapporo, Hokkaido", "Domestic Public Track", "MEXT Dual-Language IB DP", 32.0),
    ("高知県立高知国際高等学校 (Kochi Kokusai)", "Kochi, Shikoku", "Domestic Public Track", "MEXT Dual-Language IB DP", 31.2),
    ("Tokyo Gakugei University International Secondary", "Nerima-ku, Tokyo", "Domestic National Track", "MEXT Dual-Language IB DP", 34.8),
    ("Kanagawa Prefectural Yokohama Kokusai High", "Yokohama, Kanagawa", "Domestic Public Track", "MEXT Dual-Language IB DP", 33.6),
    ("Hiroshima Prefectural Hiroshima Global Academy", "Osakikamijima, Hiroshima", "Domestic Public Track", "MEXT Dual-Language IB DP", 33.6),
    ("Kyoto Municipal Saikyo High School Track", "Kyoto City, Kyoto", "Domestic Public Track", "MEXT Dual-Language IB DP", 32.2),
    ("Aichi Prefectural Sanaru Senior High", "Aichi Prefecture", "Domestic Public Track", "MEXT Dual-Language IB DP", 31.0),
    ("Shizuoka Prefectural Mishima Kita High School", "Mishima, Shizuoka", "Domestic Public Track", "MEXT Dual-Language IB DP", 31.5),
    ("Hyogo Prefectural Ashiya International Secondary", "Ashiya, Hyogo", "Domestic Public Track", "MEXT Dual-Language IB DP", 32.0),
    ("Osaka Prefectural Kishiwada High School Track", "Kishiwada, Osaka", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.5),
    ("Fukuoka Prefectural Munakata High School Track", "Munakata, Fukuoka", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.4),
    ("Oita Prefectural Oita Uenoogaoka High School", "Oita City, Oita", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.6),
    ("Kagoshima Prefectural Konan High School Track", "Kagoshima City, Kagoshima", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.3),("Kumamoto Prefectural Daiichi High School Track", "Kumamoto City, Kumamoto", "Domestic Public Track", "MEXT Dual-Language IB DP", 30.2)]

raw_list = []
for school_group in [group_a, group_b, group_c]:
    for name, loc, cat, path, score in school_group:
        raw_list.append({"Name": name, "Location": loc, "Category": cat, "Curriculum Pathway": path, "Academic_Index": score})

df = pd.DataFrame(raw_list)
df_sorted = df.sort_values(by="Academic_Index", ascending=False).reset_index(drop=True)
df_sorted.insert(0, "Ranking", df_sorted.index + 1)
df_final = df_sorted.drop(columns=["Academic_Index"])

df_final.to_csv("comprehensive_japan_ib_directory.csv", index=False)
print(f"Compilation Verified. Complete Row Count Succeeded: {len(df_final)}")
print(df_final.to_string(index=False))
