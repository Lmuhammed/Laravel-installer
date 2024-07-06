<div style="text-align: center;">

# Laravel installer 
## برنامج بايثون لأتمتة عملية تثبيت مشروع مستنسخ حديثًا من github 
## A python script to automate the process of installing a newly cloned project from github 
</div>

<div style="text-align: right;">

## الدليل بالعربية 

برنامج بايثون لتثبيت مشروع لارافل مستنسخ حديثا من جيتهوب ، حيث يقوم هذا البرنامج بتثبيت كل الإعتماديات الخاصة بتشغيل المشروع ، حيث يوم المشروع بالتالي :
<br>
- تثبيت إعتماديات البي إتش بي عن طريق ملف composer.json
<br>
- تثبيت إعتماديات package.json
<br>
- إنتاج المفاتيح عن طريق  php artisan key:generate 
<br>
- تجهيز قاعدة البيانات عن طريق php artisan migrate
<br>

### جدول المحتويات

- [التثبيت](#التثبيت)
- [الاستخدام](#الاستخدام)
- [المساهمة](#المساهمة)
- [الترخيص](#الترخيص)


### التثبيت

- قُم بتزيل المستودع 

```bash
git clone https://github.com/Lmuhammed/Laravel-installer.git
```

### الاستخدام

- قُم بالدخول إلى مجلد المُستودع 

```bash
cd Laravel-installer
```
- قم بتشغيل البرنامج 

```bash
python3 ./Laravel-installer.py
```

### المساهمة

إذا لاحظت أي مشكلة أو درت المُساهمة في التطوير ، لا تتردد في <a href="https://github.com/Lmuhammed/Laravel-installer/issues">الإبلاغ غن خطأ</a>
أو قم بنسخ المُستودع وأرسل التغييرات للمُراجعة .
### الترخيص

موزعة بموجب ترخيص GPL3. انظر 'LICENSE.txt' لمزيد من المعلومات.

</div> 

### English Manual   

A Python script to install a newly cloned Laravel project from GitHub, where this program installs all the dependencies for running the project, as the project day as follows:

- Install the PHP dependencies via the composer.json file
<br>
- Install the package.json dependencies
<br>
- Generate keys via php artisan key:generate 
<br>
- Prepare the database with php artisan migrate

#### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

#### Installation

- Open the terminal at your favorite place 

```bash
git clone https://github.com/Lmuhammed/Laravel-installer.git
```

#### Usage
- Access the project folder 

```bash
cd ./git-Bulky
```
- Run

```bash
python3 ./Laravel-installer.py
```

#### Contributing

If you notice any issues or want to contribute to the development, feel free to  <a href="https://github.com/Lmuhammed/Laravel-installer/issues">report a bug</a> or  fork the repo and commit changes as PULL REQUEST

#### License

Distributed under the GPL3 License. See `LICENSE.txt` for more information.
