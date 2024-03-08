// Data Table Pagination
$("td,th")
     .css({
         /* required to allow resizer embedding */
         position: "relative"
     })
     /* check .resizer CSS */
     .prepend("<div class='resizer'></div>")
     .resizable({
         resizeHeight: false,
         // we use the column as handle and filter
         // by the contained .resizer element
         handleSelector: "",
         onDragStart: function(e, $el, opt) {
         // only drag resizer
         if (!$(e.target).hasClass("resizer"))
             return false;
         return true;
         }
     });

function configure_action_bar(model_name)
{
    var table_id = "tbl_" + model_name;
    var table_elm =  document.getElementById(table_id);

    if (table_elm != null )
    {
        $("#"+table_id).DataTable(
            {
              "pageLength": 40,
              "scrollCollapse": true
            }
        );
        var elm_filter = document.getElementById(table_id+"_filter");
        var elm_filter_input = elm_filter.getElementsByTagName("input")[0];
        var elm_paginate = document.getElementById(table_id+"_paginate");
        var elm_info = document.getElementById(table_id+"_info");

        // Remove First Row
        var elm_row = elm_filter.parentElement.parentElement
        elm_row.parentElement.removeChild(elm_info.parentElement.parentElement)
        elm_row.parentElement.removeChild(elm_row)

        document.getElementById("div_" + model_name + "_filter").append(elm_filter_input);
        document.getElementById("div_" + model_name + "_pagination").append(elm_paginate);
    }
}

$(".panel-left").resizable({
            handleSelector: ".splitter-v",
            resizeHeight: false
     });
 $(".panel-top").resizable({
        handleSelector: ".splitter-h",
        resizeWidth: false
 });

$(document).on("click", ".show-standard-popup", function (e) {
    e.preventDefault();
    var title = $(this).data('title');
    var $popup = $("#standard_popup");
    var popup_url = $(this).data("popup-url");
    $(".modal-header #id_modal_title").text(title);
    $(".modal-body", $popup).load(popup_url, function () {
      $popup.modal("show");
    });
 });

 // Treeview Initialization
$(document).ready(function() {
  $('.treeview').mdbTreeview();
});

var rows = document.getElementsByClassName("tree-node-parent");
for(r of rows)
{
    r.addEventListener("click", function () {
    this.parentElement.querySelector(".nested").classList.toggle("active");
  });
}

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

function configSelectionEventWithContextMenu(elementId)
{
    var elm_table = document.getElementById(elementId);
    var rows = elm_table.getElementsByClassName("row-select");
    var contextMenu = document.querySelector(".menubar-wrapper");
    var shareMenu = contextMenu.querySelector(".sub-menu");

    for(r of rows)
    {
        r.style.cursor = "pointer";
        r.addEventListener("click",function(e)
        {
            var rowsNotSelected = elm_table.getElementsByClassName("row-select");
            for(r of rowsNotSelected)
            {
                r.style.background = "";
            }
            // highlight current selection
            this.style.background = "lightblue";
        });

        r.addEventListener("contextmenu", e => {
            e.preventDefault();
            var rect = e.target.getBoundingClientRect();
            let x = rect.left + 50, y = rect.top + 10;
            contextMenu.style.left = `${x}px`;
            contextMenu.style.top = `${y}px`;
            contextMenu.style.visibility = "visible";
        });
    }

    var menus = document.getElementsByClassName("menu-click");
    for(m of menus)
    {
        var action_index = m.getAttributeNode('action-index').value;
        if(action_index != null && action_index != 'NOT-DEFINE')
        {
            m.addEventListener("click",function(e)
            {
                e.preventDefault();
                var $popup = $("#standard_popup");
                var row_selection = getTableSelection(elm_table);
                var pk = row_selection.getElementsByClassName("row_id")[0];
                if (pk != null)
                {
                    var elm_menu = e.target;
                    if (elm_menu instanceof HTMLSpanElement)
                    {
                        elm_menu = elm_menu.parentElement.parentElement;
                    }
                    var action_title = elm_menu.getAttributeNode('action-title').value;
                    var action_index = elm_menu.getAttributeNode('action-index').value;
                    var action_url = elm_menu.getAttributeNode('action-url').value;
                    action_url = action_url.replace('@pk@',pk.textContent);
                    action_url = action_url.replace('context_menu',action_index);
                    $(".modal-header #id_modal_title").text(action_title);
                    $(".modal-body", $popup).load(action_url, function ()
                    {
                        $popup.modal("show");
                    });
                }
                else
                {
                    console.error('row_id class not define to identify the primary key value');
                }
            });
        }
        else
        {
            console.error('No action-url class define for this action');
        }
    }

    document.addEventListener("click", e => {
        if (contextMenu.style.visibility == "visible")
        {
            var s = e.target;
        }
	    contextMenu.style.visibility = "hidden"
    });
}

function getTableSelection(elm_parent)
{
    var rows = elm_parent.getElementsByClassName("row-select");
    for (r of rows)
    {
        if(r.style.background == "lightblue")
        {
            console.log(r.getElementsByClassName("row_id")[0].textContent);
            return r;
        }
    }
    return null;
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