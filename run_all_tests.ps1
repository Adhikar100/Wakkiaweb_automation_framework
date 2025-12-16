\
        param(
          [string]$Marker = "",
          [switch]$Headed,
          [int]$Workers = 0
        )

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }

        $xdist = ""
        if ($Workers -gt 0) { $xdist = "-n $Workers" }

        if ($Marker -ne "") {
          pytest $xdist -m $Marker
        } else {
          pytest $xdist
        }
