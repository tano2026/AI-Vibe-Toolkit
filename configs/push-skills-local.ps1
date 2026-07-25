# Auto-push local skills to GitHub & Local Sync
$RepoPath = "C:\Users\Nguyen Ngoc Tan\AI-Vibe-Toolkit"
Set-Location $RepoPath

# 1. Sync skills locally to Hermes & OpenClaw
$RootSkills = Get-ChildItem -Path "$RepoPath\skills" -Directory
foreach ($dir in $RootSkills) {
    $name = $dir.Name
    if (Test-Path "$($dir.FullName)\SKILL.md") {
        # Hermes
        $hermesDir = "C:\Users\Nguyen Ngoc Tan\AppData\Local\hermes\skills\$name"
        if (!(Test-Path $hermesDir)) { New-Item -ItemType Directory -Path $hermesDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$hermesDir\SKILL.md" -Force
        # OpenClaw
        $openclawDir = "C:\Users\Nguyen Ngoc Tan\.openclaw\skills\$name"
        if (!(Test-Path $openclawDir)) { New-Item -ItemType Directory -Path $openclawDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$openclawDir\SKILL.md" -Force
    }
}

$AgentSkills = Get-ChildItem -Path "$RepoPath\agents\*\skills\*" -Directory
foreach ($dir in $AgentSkills) {
    $name = $dir.Name
    if (Test-Path "$($dir.FullName)\SKILL.md") {
        # Hermes
        $hermesDir = "C:\Users\Nguyen Ngoc Tan\AppData\Local\hermes\skills\$name"
        if (!(Test-Path $hermesDir)) { New-Item -ItemType Directory -Path $hermesDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$hermesDir\SKILL.md" -Force
        # OpenClaw
        $openclawDir = "C:\Users\Nguyen Ngoc Tan\.openclaw\skills\$name"
        if (!(Test-Path $openclawDir)) { New-Item -ItemType Directory -Path $openclawDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$openclawDir\SKILL.md" -Force
    }
}

# 2. Add all changes & Push to GitHub
git add .

$status = git status --porcelain
if ($status) {
    $date = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    git commit -m "Auto-sync skills: $date"
    git push origin main
}
