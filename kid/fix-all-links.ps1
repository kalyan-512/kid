# Fix all remaining .html extensions in footer links across all pages
$files = @(
    'programs.html', 'contact.html', 'preschools.html', 'blog.html', 'franchise.html',
    'privacy-policy.html', 'terms-conditions.html',
    'preschool-gachibowli.html', 'preschool-nallagandla.html',  
    'preschool-attapur.html', 'preschool-begumpet.html', 'preschool-ameerpet.html'
)

$basePath = "C:\Users\kalya\Desktop\Unbilled 2\kid\kid"

foreach ($file in $files) {
    $fullPath = Join-Path $basePath $file
    if (Test-Path $fullPath) {
        $content = Get-Content $fullPath -Raw -Encoding UTF8
        
        # Fix all .html footer links
        $content = $content -replace 'href="index\.html"', 'href="/"'
        $content = $content -replace 'href="about\.html"', 'href="/about"'
        $content = $content -replace 'href="programs\.html"', 'href="/programs"'
        $content = $content -replace 'href="contact\.html"', 'href="/contact"'
        $content = $content -replace 'href="admission\.html"', 'href="/admission"'
        $content = $content -replace 'href="blog\.html"', 'href="/blog"'
        $content = $content -replace 'href="franchise\.html"', 'href="/franchise"'
        $content = $content -replace 'href="preschools\.html"', 'href="/preschools"'
        $content = $content -replace 'href="privacy-policy\.html"', 'href="/privacy-policy"'
        $content = $content -replace 'href="terms-conditions\.html"', 'href="/terms-conditions"'
        
        # Save with UTF8 encoding
        [System.IO.File]::WriteAllText($fullPath, $content, [System.Text.UTF8Encoding]::new($false))
        Write-Host "✅ Fixed: $file"
    }
}

Write-Host "`n🎉 All footer links fixed!"
