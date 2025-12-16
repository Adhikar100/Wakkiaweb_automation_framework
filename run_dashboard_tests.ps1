\
        param(
          [string]$Marker = "dashboard",
          [switch]$Headed,
          [switch]$Trace
        )

        if (-not (Test-Path ".venv")) {
          Write-Host " .venv not found. Create venv first." -ForegroundColor Red
          exit 1
        }

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }
        if ($Trace) { $env:TRACE="true" }

        pytest dashboard_app/tests -m $Marker
