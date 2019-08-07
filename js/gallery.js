$(function(){
    opacity();

    $.getJSON( "/Watson-web/images/gallery/gallery.json", function( data ) {
        populate(data);
    });

});
/***
 * change the opacity of the image based on hover state
 */
function opacity(){
    let expand = $(".expand");
    expand.hover(function(){
        console.log("mouse in");
        $('.expand').prev().css('opacity','0.7');
    });
    expand.mouseleave(function(){
        console.log("mouse out");
        $('.expand').prev().css('opacity','1');
    });


    let image =$(".image");
    image.hover(function(){
        console.log("mouse in");
        $(this).css('opacity','0.7');
    });
    image.mouseleave(function(){
        console.log("mouse in");
        $(this).css('opacity','1');
    });
}
function populate(data) {
    let data_size = data.length;
    let counter =0;
    while (counter < data_size){
        $(".enlarge").after(
            "<div class='col-lg-3 col-md-3 col-sm-12 img-div'><img src='"+ data[counter].source+ "' class='image'><span class='expand'>"+data[counter].name+"</span></div>"
        );
        counter++;
    }
}