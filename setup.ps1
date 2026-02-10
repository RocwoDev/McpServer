# Installation script for MCP Web Utilities Server

function Install-Uv {
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        Write-Host "uv is already installed." -ForegroundColor Green
    } else {
        Write-Host "Installing uv..." -ForegroundColor Cyan
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    }
}

function Setup-Project {
    Write-Host "Syncing dependencies with uv..." -ForegroundColor Cyan
    uv sync
    if ($LASTEXITCODE -ne 0) {
        Write-Error "uv sync failed."
        exit $LASTEXITCODE
    }

    Write-Host "Setting up crawl4ai..." -ForegroundColor Cyan
    # Use 'uv run' to ensure crawl4ai-setup is executed within the virtual environment context
    uv run crawl4ai-setup
    if ($LASTEXITCODE -ne 0) {
        Write-Error "crawl4ai-setup failed."
        exit $LASTEXITCODE
    }
}

Install-Uv
Setup-Project

Write-Host "Installation completed successfully!" -ForegroundColor Green
Write-Host "You can now start the server with: uv run src\main.py"
