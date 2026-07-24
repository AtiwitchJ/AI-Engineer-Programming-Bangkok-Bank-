# โครงสร้างระบบ Multi-Agent + RAG

> Bangkok Bank — AI Engineer Programming Test

## Flowchart

```mermaid
flowchart LR
    U["ผู้ใช้<br/>คำถาม"] --> DR["Data Retriever<br/>(RAG)"]
    DR -->|"เรียก tool"| T["search tool"]
    T --> KB[("knowledge_base.txt")]
    T -->|"ข้อความที่เกี่ยวข้อง<br/>(raw text เท่านั้น)"| DR
    DR -->|"ส่งต่อ snippets<br/>ไม่ตอบเอง"| RG["Report Generator"]
    RG -->|"คำตอบครบ / ไม่ซ้ำ / จัดรูปแบบ"| U
```

## ความรับผิดชอบของ Agent

| Agent | ความรับผิดชอบ |
|-------|----------------|
| **Data Retriever** *(RAG)* | ค้นหาข้อมูลเฉพาะเจาะจงจากฐานความรู้ โดย **ไม่ตอบคำถามเอง** — จะส่งคืนเฉพาะข้อความที่เกี่ยวข้องเท่านั้น |
| **Report Generator** | รับข้อความจาก Data Retriever แล้วเรียบเรียงเป็นคำตอบที่ครบถ้วน ไม่ซ้ำซ้อน และจัดรูปแบบสวยงามให้ผู้ใช้ |
