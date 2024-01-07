    function configSelectionEvent(elementId)
    {
        var elm_parent = document.getElementById(elementId);

        var rows = elm_parent.getElementsByClassName("row-select");
        for(r of rows)
        {
            r.style.cursor = "pointer";
            r.addEventListener("click",function()
            {
                var rowsNotSelected = elm_parent.getElementsByClassName("row-select");
                for(r of rowsNotSelected)
                {
                    r.style.background = "";
                }

                // highlight current selection
                this.style.background = "lightblue";
            });
        }
    }

    function configOnSelectionView(elementId,data_url,data_view_id)
    {
        var elm_parent = document.getElementById(elementId);
        var rows = elm_parent.getElementsByClassName("row-select");
        for(r of rows)
        {
            r.addEventListener("click",function()
            {
                var view_id = '#'+data_view_id;
                alert(this.querySelector(".node-value").textContent);
                // AJax Call
                $.ajax({
                    type: "GET",
                    url: data_url,  // URL to your view that serves new info
                    data: {'row_id': this.querySelector(".node-value").textContent.trim()}
                })
                .done(function(response) {
                    $(view_id).html(response);
                });
            });
        }
    }

    alert("debug2");
    function findParentByClass(el,class_name)
    {
        while (el.parentElement)
        {
            el = el.parentElement;
            if (el.classList.contains(class_name))
                return el;
        }
        return null;
    }