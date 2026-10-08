# ระบบวิเคราะห์อารมณ์ข้อความแบบประเมินคำหลัก (Keyword-Based Sentiment)
positive_words = ["สนุก", "ดี", "ชอบ", "เข้าใจง่าย", "สำเร็จ", "เยี่ยม"]
negative_words = ["ค้าง", "ห่วย", "ช้า", "ไม่ได้", "แย่", "ติดขัด"]

def analyze_sentiment(text):
    pos_count = sum(1 for word in positive_words if word in text)
    neg_count = sum(1 for word in negative_words if word in text)
    
    if pos_count > neg_count:
        return "😊 เชิงบวก (Positive)"
    elif neg_count > pos_count:
        return "😡 เชิงลบ (Negative)"
    else:
        return "😐 ไม่ระบุ/ทั่วไป (Neutral)"

# ทดสอบรันผลลัพธ์
print("--- เริ่มต้นระบบ AI วิเคราะห์อารมณ์จากข้อความ --- \n")
msg1 = "สาขานี้เรียนสนุกมาก อาจารย์สอนเข้าใจง่ายที่สุด"
msg2 = "ระบบแอปพลิเคชันค้างบ่อยมาก ใช้งานไม่ได้เลย ห่วยสุดๆ"
print(f"ข้อความ: \"{msg1}\" \nผลทำนาย: {analyze_sentiment(msg1)}\n")
print(f"ข้อความ: \"{msg2}\" \nผลทำนาย: {analyze_sentiment(msg2)}\n")
