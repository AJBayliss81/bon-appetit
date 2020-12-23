$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $('.modal').modal();
    $(".dropdown-trigger").dropdown();
    $(".dropdown-content li a").css({"background-color": "#4c5c68", "color": "#c5c3c6"});
    $(".tooltipped").tooltip();
    $("select").formSelect();

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #388e3c", "box-shadow": "0 1px 0 0 #388e3c" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

/*---- Show/hide buttons ----*/

$("#cuisinesToggle").click(function() {
    if($(this).text()=="Show Cuisines ")
    {
        $(this).html("Hide Cuisines <i class='fas fa-minus-square'></i>");
    } else {
        $(this).html("Show Cuisines <i class='fas fa-plus-square'></i>");
    }
    $("#cuisines").toggle("slow"); 

    return false;
});

$("#ingredientsToggle").click(function() {
    if($(this).text()=="Show Ingredients ")
    {
        $(this).html("Hide Ingredients <i class='fas fa-minus-square'></i>");
    } else {
        $(this).html("Show Ingredients <i class='fas fa-plus-square'></i>");
    }
    $("#ingredients").toggle("slow"); 

    return false;
});

$("#methodToggle").click(function() {
    if($(this).text()=="Show Method ")
    {
        $(this).html("Hide Method <i class='fas fa-minus-square'></i>");
    } else {
        $(this).html("Show Method <i class='fas fa-plus-square'></i>");
    }
    $("#method").toggle("slow"); 

    return false;
});

/*---- Dropdown mouseover/out ----*/

$(".dropdown-content li a").mouseover(function() {
    $(this).css("background-color", "#46494c");
});
$(".dropdown-content li a").mouseout(function() {
    $(this).css("background-color", "#4c5c68");
});


/*---- Buttons mouseover/out ----*/

$(".btn-small").mouseover(function() {
    $(this).addClass("hover");
});
$(".btn-small").mouseout(function() {
    $(this).removeClass("hover");
});
