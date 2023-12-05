<template>
    <section class="testimonial flex bg-accent-quaternary py-12 lg:min-h-[595px] lg:py-0">
        <div class="testimonial_container flex lg:justify-center xl:bg-services 
        lg:bg-none xl:bg-no-repeat xl:bg-cover xl:justify-end items-center container 
        mx-auto">
        <!-- SLIDER -->
        <div class="max-w-[98%] lg:max-w-[710px]">
            <!-- Slider main container -->
            <div class="swiper h-[450px]">
            <!-- Additional required wrapper -->
            <div class="swiper-wrapper">
                <!-- Slide1 -->
                <div class="swiper-slide">
                <div class="h-full  flex flex-col justify-center items-start">
                    <div class="max-w-[680px] mx-auto text-center lg:text-left">
                    <!-- MESSAGE -->
                    <p class="font-light relative text-[22px] text-[#4c5354]
                        leading-[190%] text-center lg:text-left before:bg-quoteLeft
                        before:bg-contain before:bg-bottom before:inline-block
                        before:top-0 before:w-10 before:h-10 before:bg-no-repeat
                        after:bg-quoteRight
                        after:bg-contain after:bg-bottom after:inline-block
                        after:top-0 after:w-10 after:h-10 after:bg-no-repeat mb-7">
                        <span class="mx-2">
                            Outstanding experience! The surgical team provided expert care with compassion and precision. The recovery was smooth, thanks to their attentive follow-up. Highly recommend MedCenter for excellent surgical outcomes and support.
                    </span>
                    </p>
                    <!-- NAME -->
                    <div class="text-[26px] text-[#4c5354] font-semibold">Carl Dather</div>
                    <!-- JOB -->
                    <div class="text-[#9ab4b7] font-medium uppercase tracking-[2.24px]">Patient</div>
                    </div>
                </div>
                </div>
                <!-- Slide2 -->
                <div class="swiper-slide">
                <div class="h-full  flex flex-col justify-center items-start">
                    <div class="max-w-[680px] mx-auto text-center lg:text-left">
                    <!-- MESSAGE -->
                    <p class="font-light relative text-[22px] text-[#4c5354]
                        leading-[190%] text-center lg:text-left before:bg-quoteLeft
                        before:bg-contain before:bg-bottom before:inline-block
                        before:top-0 before:w-10 before:h-10 before:bg-no-repeat
                        after:bg-quoteRight
                        after:bg-contain after:bg-bottom after:inline-block
                        after:top-0 after:w-10 after:h-10 after:bg-no-repeat mb-7">
                        <span class="mx-2">
                            The staff was professional, caring, and attentive throughout the entire process. The care and attention to detail made a significant difference. Highly recommend this center for top-quality medical treatment!
                        </span>
                    </p>
                    <!-- NAME -->
                    <div class="text-[26px] text-[#4c5354] font-semibold">Jane Huwitz</div>
                    <!-- JOB -->
                    <div class="text-[#9ab4b7] font-medium uppercase tracking-[2.24px]">Customer</div>
                    </div>
                </div>
                </div>
                <!-- Slide3 -->
                <div class="swiper-slide">
                <div class="h-full  flex flex-col justify-center items-start">
                    <div class="max-w-[680px] mx-auto text-center lg:text-left">
                    <!-- MESSAGE -->
                    <p class="font-light relative text-[22px] text-[#4c5354]
                        leading-[190%] text-center lg:text-left before:bg-quoteLeft
                        before:bg-contain before:bg-bottom before:inline-block
                        before:top-0 before:w-10 before:h-10 before:bg-no-repeat
                        after:bg-quoteRight
                        after:bg-contain after:bg-bottom after:inline-block
                        after:top-0 after:w-10 after:h-10 after:bg-no-repeat mb-7">
                        <span class="mx-2">
                            Impressive service and care! The team was professional, friendly, and attentive, making the entire experience smooth and reassuring. Highly recommend this center for exceptional medical care and support.
                        </span>
                    </p>
                    <!-- NAME -->
                    <div class="text-[26px] text-[#4c5354] font-semibold">Brad Porter</div>
                    <!-- JOB -->
                    <div class="text-[#9ab4b7] font-medium uppercase tracking-[2.24px]">Customer</div>
                    </div>
                </div>
                </div>
            </div>
            <!-- If we need pagination -->
            <div class="swiper-pagination"></div>
            </div>
        </div>
        </div>
    </section>

</template>

<script>
    export default {
        mounted() {
            // Initialize ScrollReveal
            import('scrollreveal').then(ScrollReveal => {
            const sr = ScrollReveal.default({
                origin: 'bottom',
                distance: '30px',
                duration: 1000,
                delay: 100
            });
            
            sr.reveal('.testimonial', {interval: 200});
            sr.reveal('.testimonial_container', {interval: 200});

            });
        }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
