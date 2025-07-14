# تغییر Execution Policy برای کاربر فعلی (در صورت نیاز)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# بررسی وجود پوشه venv
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    & ".\venv\Scripts\Activate.ps1"
    Write-Host "✅ محیط مجازی با موفقیت فعال شد! برای خروج دستور deactivate را بزنید." -ForegroundColor Green
} else {
    Write-Host "❌ پوشه venv پیدا نشد! لطفاً اول محیط مجازی را با دستور python -m venv venv بسازید." -ForegroundColor Red
}
