let parentCompanyrows = $('.field_370')
for(i=1; i < parentCompanyrows.length; i++){
  $('.field_534').eq(i).val(parentCompanyrows.eq(i).text());
}
