\
        param(
          [string]$Marker = "customer",
          [switch]$Headed,
          [switch]$Trace
        )

        if (-not (Test-Path ".venv")) {
          Write-Host "❌ .venv not found. Create venv first." -ForegroundColor Red
          exit 1
        }

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }

        # Optional trace toggle (you can wire this later into browser_factory)
        if ($Trace) { $env:TRACE="true" }

        pytest customer_app/tests -m $Marker
