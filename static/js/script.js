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
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
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

$(".profile-dd").mouseover(function() {
    $('.profile-dd').css("background-color", "#46494c");
});
$(".profile-dd").mouseout(function() {
    $('.profile-dd').css("background-color", "#4c5c68");
});

$(".browse-dd").mouseover(function() {
    $('.browse-dd').css("background-color", "#46494c");
});
$(".browse-dd").mouseout(function() {
    $('.browse-dd').css("background-color", "#4c5c68");
});

$(".add-dd").mouseover(function() {
    $('.add-dd').css("background-color", "#46494c");
});
$(".add-dd").mouseout(function() {
    $('.add-dd').css("background-color", "#4c5c68");
});

$(".recipe-dd").mouseover(function() {
    $('.recipe-dd').css("background-color", "#46494c");
});
$(".recipe-dd").mouseout(function() {
    $('.recipe-dd').css("background-color", "#4c5c68");
});

$(".admin-dd").mouseover(function() {
    $('.admin-dd').css("background-color", "#46494c");
});
$(".admin-dd").mouseout(function() {
    $('.admin-dd').css("background-color", "#4c5c68");
});
