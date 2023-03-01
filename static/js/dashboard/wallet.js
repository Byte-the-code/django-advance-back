const swiperSlides = document.querySelectorAll('.swiper-slide');

swiperSlides.forEach(slide => {
  slide.addEventListener('click', () => {
    const cardNameSlide = slide.querySelector('.card_name').innerText;
    const validUntilSlide = slide.querySelector('.valid_until').innerText;
    const cardNumberSlide = slide.querySelector('.card_number').innerText;
    const bankNameSlide = slide.querySelector('.bank_name').innerText;
    const cardHolderSlide = slide.querySelector('.card_holder').innerText;

      const mainBalance = document.querySelector('#main-balance')
      const validDate = document.querySelector('#valid-date')
      const cardNumber = document.querySelector('#card-number')
      const bankName = document.querySelector('#bank-name')
      const cardHolder = document.querySelector('#card-holder')

    mainBalance.textContent = cardNameSlide
    validDate.textContent = validUntilSlide
    cardNumber.textContent = cardNumberSlide
    bankName.textContent = bankNameSlide
    cardHolder.textContent = cardHolderSlide
  });
})