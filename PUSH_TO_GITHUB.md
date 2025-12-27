# 📤 تعليمات رفع المشروع المنظم إلى GitHub

## الخطوات:

### 1. تأكد من أنك في مجلد المشروع:
```bash
cd "/home/joo/New Folder/Real-Time_NYC_Transit_Monitoring"
```

### 2. تهيئة Git (إذا لم يكن موجوداً):
```bash
git init
```

### 3. إضافة المستودع البعيد:
```bash
git remote remove origin 2>/dev/null
git remote add origin https://github.com/Y0U5F/Real-Time_NYC_Transit_Monitoring.git
```

### 4. إضافة جميع الملفات:
```bash
git add -A
```

### 5. إنشاء Commit:
```bash
git commit -m "Initial commit: Organized project structure

- Organized code into src/pipeline with proper structure
- Separated ingestion, bronze, silver, and gold layers
- Moved documentation to docs/ folder
- Added requirements.txt and .gitignore
- Updated all file paths to work with new structure
- All original code logic preserved"
```

### 6. تعيين Branch الرئيسي:
```bash
git branch -M main
```

### 7. رفع المشروع إلى GitHub:
```bash
git push -u origin main --force
```

**ملاحظة:** قد تحتاج إلى إدخال اسم المستخدم وكلمة المرور أو Personal Access Token من GitHub.

---

## أو استخدم السكريبت الجاهز:

```bash
chmod +x push_organized_project.sh
./push_organized_project.sh
```

---

## بعد الرفع:

تحقق من المستودع على:
https://github.com/Y0U5F/Real-Time_NYC_Transit_Monitoring

