function onlySpaces(str)
{
    return str.trim().length === 0;
}

$(document).ready(function()
{
    $("form").on("submit",function(event)
    {
        var date1 = document.getElementById("date1").value;
        var date2 = document.getElementById("date2").value;
        if (onlySpaces(date1) == false && onlySpaces(date2) == false)
        {
            document.getElementById("resultdiv").setAttribute("hidden",false);
            document.getElementById("loading").removeAttribute("hidden");
            $.ajax({
                data:{
                    date1:date1,
                    date2:date2,
                },
                type: "POST",
                url: "/submit",
            }).done(function(data)
            {
                result = data;
                document.getElementById("loading").setAttribute("hidden",false);
                document.getElementById("result").innerHTML = result;
                document.getElementById("resultdiv").removeAttribute("hidden");
            });
        }
        else{
            document.getElementById("resultdiv").setAttribute("hidden",false);
        }
    event.preventDefault();
    });
});
