<template>
    <header class="py-8 lg:pt-6 lg:pb-14 bg-[#EBE9E1]">
        <div class="container mx-auto lg:relative flex flex-col lg:flex-row lg:justify-between gap-y-4 lg:gap-y-0">
            <div class="flex justify-center lg:justify-normal">
                <h1 class="text-5xl lg:text-left font-bold relative">
                    Med<b class="text-accent">Center</b><br />
                    
                </h1>
            </div>
            <div class="flex flex-col gap-y-4 lg:flex-row lg:gap-x-5 lg:gap-y-0 items-center">
                <div class="flex gap-x-2">
                    <i class="ri-map-pin-2-fill text-2xl text-accent"></i>
                    <div>Los Delfines 43622, MI</div>
                </div>
                <div class="flex gap-x-2">
                    <i class="ri-phone-fill text-2xl text-accent"></i>
                    <div>(+51) 43 249 01</div>
                </div>
                <button class="btn btn-sm btn-outline w-[240px] lg:2-auto mx-auto lg:mx-0">Book now</button>
                <nav class="mnav fixed top-0 -left-[300px] h-full w-[300px] bg-white lg:hidden shadow-2xl transition-all duration-300 z-20">
                    <div class="mnav_close_btn bg-primary w-8 lg:w-[45px] relative -right-full lg:-right-[45px] top-8 flex justify-center items-center rounded-tr-lg rounded-br-lg cursor-pointer transition-all" @click="toggleMobileNav">
                    <i class="mnav_close_btn_icon ri-arrow-right-s-line text-white text-2xl"></i>
                    </div>
                    <div class="px-12 flex flex-col gap-y-12 h-full">
                    <a href="#">
                        <div class="flex justify-center lg:justify-normal">
                        <h1 class="text-5xl lg:text-left font-bold relative">
                            In<b class="text-accent">sove</b><br />
                            <small class="text-secondary text-[12px] font-normal absolute top-[2.7rem] left-0 lg:text-[12px]">Medical Healthcare</small>
                        </h1>
                        </div>
                    </a>
                    </div>
                </nav>
            </div>
        </div>
    </header>
</template>
  
<script>
    export default {
    methods: {
        toggleMobileNav() {
        const mobileNav = document.querySelector('.mnav');
        const closeBtnIcon = document.querySelector('.mnav_close_btn_icon');
        const navOpenedClass = 'left-0';
        const navClosedClass = '-left-[300px]';
        const arrowLeftClass = 'ri-arrow-left-s-line';
        const arrowRightClass = 'ri-arrow-right-s-line';

        mobileNav.classList.toggle(navOpenedClass);
        mobileNav.classList.toggle(navClosedClass);
        closeBtnIcon.classList.toggle(arrowLeftClass);
        closeBtnIcon.classList.toggle(arrowRightClass);
        }

    }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
