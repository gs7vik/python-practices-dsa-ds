import re

def build_target_lookup(sample_data):
    target_lookup = {}
    
    pattern = re.compile(
        r'"(?P<target>Target_\d+_Main) is also called (?P<synonyms>.*?)(?: and its a (?P<type>\w+))', re.IGNORECASE)

    print(pattern.pattern)  # Debugging line to check the regex pattern
    for match in pattern.finditer(sample_data):
        target = match.group("target")
        synonyms = [s.strip() for s in match.group("synonyms").split(",")]
        type_ = match.group("type").lower()
        
        target_lookup[target.lower()] = {"synonyms": synonyms, "type": type_}
        
        
        for synonym in synonyms:
            target_lookup[synonym.lower()] = {"synonyms": synonyms, "type": type_}
    
    return target_lookup

def rephrase_query(question, lookup):
    question_lower = question.lower()
    
    for key in lookup:
        if key in question_lower:
            target_info = lookup[key]
            synonyms = target_info["synonyms"]
            type_ = target_info["type"]
            
            
            for s in synonyms:
                if s.lower() in question_lower:
                    found = s
                    break
            else:
                found = key
            
            # Create the rephrased query
            replacement = f"{found} (also known as {', '.join(synonyms)})"
            rephrased_query = question.replace(found, replacement)
            
            return {
                "rephrased_query": rephrased_query,
                "type": [type_]
            }
    
    return {
        "rephrased_query": question,
        "type": []
    }


sample_data = """
"Target_1_Main is also called C9590, ZL1197, D6002 and its a antibody and it was discovered on 04 March 2017"
"Target_2_Main is also called B7348, A9780, MN6145, D4218 and its a bacteria and it was discovered on 13 April 12 AM"
"Target_3_Main is also called B1558, D4055 and its a gene and it was discovered on 30 September 2012 00:00 hours"
"Target_4_Main is also called A5265, MN9664, XY1419, XY5730 and its a peptide and it was discovered on 26 July 2011"
"Target_5_Main is also called A8963, D5787, B1164, D7437 and its a antibody and it was discovered on 03-08-2017 00:00"
"Target_6_Main is also called C7026, D3813, XY1805 and its a receptor and it was discovered on 23-12-2010 00:00"
"Target_7_Main is also called ZL3476, PQ5630, ZL3018 and its a gene and it was discovered on 25 September 2014"
"Target_8_Main is also called PQ2331, MN4104 and its a receptor and it was discovered on 03 May 2010"
"Target_9_Main is also called MN9834, D3101 and its a antibody and it was discovered on 14 June 2012 00:00 hours"
"Target_10_Main is also called D6543, B8079, XY3350, XY9504 and its a peptide and it was discovered on 01-09-2015 00:00"
"Target_11_Main is also called XY3674, PQ9346 and its a protein and it was discovered on 19-04-2010 00:00"
"Target_12_Main is also called XY6286, MN3105, XY4339 and its a receptor and it was discovered on 25-03-2012 00:00"
"Target_13_Main is also called C1831, XY7610 and its a receptor and it was discovered on 15 September 2014 00:00 hours"
"Target_14_Main is also called PQ9795, ZL6668, XY3611 and its a hormone and it was discovered on 14-01-2015 00:00"
"Target_15_Main is also called A5684, D9957, PQ8628 and its a toxin and it was discovered on 13 February 2013"
"Target_16_Main is also called PQ9838, A1701, D1861, PQ1134 and its a bacteria and it was discovered on 06 July 2018 00:00 hours"
"Target_17_Main is also called A2229, ZL9896 and its a virus and it was discovered on October 30, 2017"
"Target_18_Main is also called PQ6616, A7061, D2974 and its a protein and it was discovered on 25 October 12 AM"
"Target_19_Main is also called MN8408, A7081 and its a peptide and it was discovered on 29 September 2011 00:00 hours"
"Target_20_Main is also called A8991, B1742, ZL3192 and its a protein and it was discovered on 25 July 12 AM"
"Target_21_Main is also called D3693, XY7771, MN2819, C9553 and its a bacteria and it was discovered on 23 February 2011"
"Target_22_Main is also called PQ6869, D6051 and its a enzyme and it was discovered on 06 April 2014"
"Target_23_Main is also called B2992, C5176, A9544 and its a virus and it was discovered on 10 January 12 AM"
"Target_24_Main is also called C3820, PQ2505, XY4308 and its a receptor and it was discovered on 08 October 12 AM"
"Target_25_Main is also called A5595, ZL8617, A8149 and its a antibody and it was discovered on 19 January 2019"
"Target_26_Main is also called XY4224, XY5689 and its a hormone and it was discovered on March 08, 2018"
"Target_27_Main is also called ZL5179, A8627 and its a bacteria and it was discovered on 06 January 2016"
"Target_28_Main is also called MN5986, D2140, ZL5530 and its a gene and it was discovered on 31 March 2014"
"Target_29_Main is also called C4337, D8845 and its a virus and it was discovered on 11 March 12 AM"
"Target_30_Main is also called B4994, XY7292, XY9830 and its a antibody and it was discovered on 21-04-2019 00:00"
"Target_31_Main is also called D7724, PQ4429 and its a toxin and it was discovered on 06 December 12 AM"
"Target_32_Main is also called B8109, C4666, XY1374 and its a gene and it was discovered on 22 June 2016 00:00 hours"
"Target_33_Main is also called ZL9011, A4839 and its a peptide and it was discovered on 25 November 2017"
"Target_34_Main is also called PQ1246, B8815, XY4153 and its a hormone and it was discovered on 07 July 2010 00:00 hours"
"Target_35_Main is also called C1190, XY8823 and its a receptor and it was discovered on 02 September 12 AM"
"Target_36_Main is also called B1926, D7197, A3517 and its a protein and it was discovered on 23 November 2010 00:00 hours"
"Target_37_Main is also called XY3686, MN7123 and its a enzyme and it was discovered on 20 September 2019"
"Target_38_Main is also called D5103, A9326, ZL5073 and its a bacteria and it was discovered on 06 April 12 AM"
"Target_39_Main is also called B7487, C8040, MN3311 and its a antibody and it was discovered on 01 February 12 AM"
"Target_40_Main is also called MN7337, ZL3172, XY4046 and its a virus and it was discovered on 29 October 12 AM"
"Target_41_Main is also called C9332, PQ4562, A2703 and its a hormone and it was discovered on 26 December 2013 00:00 hours"
"Target_42_Main is also called PQ5679, D4601 and its a protein and it was discovered on 08 July 12 AM"
"Target_43_Main is also called XY5632, B3855, ZL9942 and its a receptor and it was discovered on 14 November 2017"
"Target_44_Main is also called A3993, MN5294, D7326 and its a gene and it was discovered on 31 October 2016 00:00 hours"
"Target_45_Main is also called B1731, C6267 and its a peptide and it was discovered on 28 December 2015 00:00 hours"
"Target_46_Main is also called PQ1282, ZL6445, B9032 and its a toxin and it was discovered on November 01, 2011"
"Target_47_Main is also called MN7245, A1475 and its a virus and it was discovered on 04 April 12 AM"
"Target_48_Main is also called D9008, C2417 and its a antibody and it was discovered on 06-03-2017 00:00"
"Target_49_Main is also called XY2884, A3128, B1654 and its a protein and it was discovered on 18 June 12 AM"
"Target_50_Main is also called PQ9453, ZL7772, XY3202 and its a bacteria and it was discovered on 15 June 2019"
"Target_51_Main is also called C4526, A7861, XY7280 and its a receptor and it was discovered on 27 July 2012"
"Target_52_Main is also called ZL2273, B9145, PQ3384 and its a enzyme and it was discovered on 11 January 12 AM"
"Target_53_Main is also called B6433, MN1682 and its a hormone and it was discovered on 02 July 12 AM"
"Target_54_Main is also called XY7029, A2853 and its a toxin and it was discovered on 29 September 2010 00:00 hours"
"Target_55_Main is also called D6832, C3246, ZL8383 and its a virus and it was discovered on 12 May 12 AM"
"Target_56_Main is also called MN4701, PQ5166, XY2398 and its a peptide and it was discovered on May 20, 2012"
"Target_57_Main is also called A1452, C2968 and its a receptor and it was discovered on June 09, 2014"
"Target_58_Main is also called PQ8032, XY1937 and its a gene and it was discovered on 09 August 12 AM"
"Target_59_Main is also called ZL4283, B7273, D3091 and its a protein and it was discovered on 26 July 2011 00:00 hours"
"Target_60_Main is also called A3657, MN5378, PQ9774 and its a antibody and it was discovered on 10-05-2018 00:00"
"Target_61_Main is also called C8460, D7723 and its a bacteria and it was discovered on 17 January 12 AM"
"Target_62_Main is also called B9921, XY4182 and its a enzyme and it was discovered on 18-05-2018 00:00"
"Target_63_Main is also called ZL1029, A5304, XY8751 and its a hormone and it was discovered on 21-10-2014 00:00"
"Target_64_Main is also called MN1722, B2675 and its a toxin and it was discovered on 24 June 12 AM"
"Target_65_Main is also called PQ7557, C6748, D4583 and its a virus and it was discovered on 17 June 2012 00:00 hours"
"Target_66_Main is also called B8331, A2884 and its a peptide and it was discovered on September 19, 2015"
"Target_67_Main is also called XY7196, PQ4792, C5923 and its a gene and it was discovered on 08 January 2011"
"Target_68_Main is also called A1197, D9625 and its a receptor and it was discovered on 29 August 2019"
"Target_69_Main is also called ZL1134, MN6817, XY5932 and its a bacteria and it was discovered on 19 September 2011 00:00 hours"
"Target_70_Main is also called D3786, B3901, C1436 and its a protein and it was discovered on November 19, 2018"
"Target_71_Main is also called PQ6193, A7120 and its a antibody and it was discovered on 08 September 2016"
"Target_72_Main is also called MN3907, ZL9124, XY5011 and its a enzyme and it was discovered on April 26, 2014"
"Target_73_Main is also called C1135, D5879 and its a hormone and it was discovered on September 06, 2016"
"Target_74_Main is also called B4241, PQ3321, A1988 and its a gene and it was discovered on 08 December 12 AM"
"Target_75_Main is also called ZL6152, XY1085 and its a peptide and it was discovered on 16 March 2016"
"Target_76_Main is also called D2341, C4997, MN7761 and its a virus and it was discovered on 18 August 2017"
"Target_77_Main is also called B6712, A6766 and its a receptor and it was discovered on 24-08-2017 00:00"
"Target_78_Main is also called PQ4319, XY9604, D5517 and its a protein and it was discovered on 03 June 12 AM"
"Target_79_Main is also called MN8592, A5041 and its a antibody and it was discovered on 15 August 12 AM"
"Target_80_Main is also called C8865, B1738, ZL3009 and its a bacteria and it was discovered on 02 April 12 AM"
"Target_81_Main is also called XY4923, PQ1872 and its a enzyme and it was discovered on 16 November 2014 00:00 hours"
"Target_82_Main is also called D1457, A7623, B9987 and its a hormone and it was discovered on 02 February 2015"
"Target_83_Main is also called MN2430, ZL7869 and its a toxin and it was discovered on 05 February 12 AM"
"Target_84_Main is also called C5743, PQ9208 and its a virus and it was discovered on 13 August 2015 00:00 hours"
"Target_85_Main is also called B5381, D1925, XY6190 and its a receptor and it was discovered on 11 September 2015"
"Target_86_Main is also called PQ1222, ZL4540 and its a gene and it was discovered on 06 October 12 AM"
"Target_87_Main is also called MN5357, A1002 and its a peptide and it was discovered on 10-06-2019 00:00"
"Target_88_Main is also called C3832, XY3517, B7708 and its a protein and it was discovered on 30 October 2016 00:00 hours"
"Target_89_Main is also called D2764, ZL8425, A7449 and its a antibody and it was discovered on 19 September 12 AM"
"Target_90_Main is also called PQ6521, C1184 and its a bacteria and it was discovered on 21 July 2018 00:00 hours"
"Target_91_Main is also called MN9082, D7106, B2381 and its a enzyme and it was discovered on 19-01-2016 00:00"
"Target_92_Main is also called A4023, XY4142 and its a hormone and it was discovered on 03-01-2010 00:00"
"Target_93_Main is also called ZL6541, PQ7274 and its a toxin and it was discovered on August 20, 2013"
"Target_94_Main is also called B5517, D8338, A9815 and its a virus and it was discovered on 21 March 2010"
"Target_95_Main is also called C7090, XY8826, ZL3277 and its a gene and it was discovered on 26 January 12 AM"
"Target_96_Main is also called MN4322, PQ3132 and its a peptide and it was discovered on 07 September 2012"
"Target_97_Main is also called XY1659, A6633 and its a receptor and it was discovered on 13-09-2012 00:00"
"Target_98_Main is also called D6024, ZL7188, C8931 and its a protein and it was discovered on 19 November 2010"
"Target_99_Main is also called B2933, MN7283 and its a antibody and it was discovered on March 17, 2018"
"Target_100_Main is also called PQ1762, A8192, XY5204 and its a bacteria and it was discovered on 25 February 2019"
"""
lookup = build_target_lookup(sample_data)

query = "Can you provide details about A2229?"
result = rephrase_query(query, lookup)

print(result)
