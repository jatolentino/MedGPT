<template>
    <section class="departments section">
        <div class="departments_bg bg-accent-quaternary max-w-[1466px] mx-4 lg:mx-auto 
        rounded-[20px] px-6 lg:px-0 py-12 lg:pt-[80px] lg:pb-[90px] relative min-h-[588px] 
        flex items-center">
        <div class="departments_container container mx-auto">
            <div class="flex flex-col lg:flex-row gap-x-5 lg:justify-around">
            <div class="lg:w-[210px] flex flex-col gap-y-[30px] lg:gap-y-[40px] 
            font-medium uppercase text-center lg:text-left text-base text-[#9ab4b7]">
                <div class="cursor-pointer hover:text-accent transition-all">
                Laboratory Analysis
                </div>
                <div class="cursor-pointer hover:text-accent transition-all">
                Cardiology Clinic
                </div>
                <div class="cursor-pointer hover:text-accent transition-all">
                Gynecology Clinic
                </div>
                <div class="cursor-pointer hover:text-accent transition-all">
                Surgical Clinic
                </div>
                <div class="cursor-pointer hover:text-accent transition-all">
                Neurology Clinic
                </div>
                <div class="cursor-pointer hover:text-accent transition-all">
                Orthopedic Clinic
                </div>
            </div>
            <div class="lg:w-[840px] mt-5 lg:mt-0">
                <!-- TITLE -->
                <h2 class="h2 mb-[20px] text-center lg:text-left">Surgical Clinic</h2>
                <!-- TEXT -->
                <p class="mb-[30px] font-light text-center lg:text-left">
                    Nestled within the heart of our medical center, the surgical clinic offers state-of-the-art facilities, advanced technology, and a team of expert surgeons dedicated to precision and care.
                <br /><br />
                    Our clinic ensures a seamless experience with personalized pre- and post-operative support, providing a comfortable, efficient environment for a wide range of specialized surgical procedures.
                </p>
                <div class="flex flex-col lg:flex-row items-center lg:justify-between
                    max-w-[555px] mb-[50px] mx-auto lg:mx-0">
                <div class="text-accent lg:border-r border-[#dcdcdc] lg:pr-4">Precision Surgery</div>
                <div class="text-accent lg:border-r border-[#dcdcdc] lg:pr-4">Expert Care</div>
                <div class="text-accent lg:pr-4">Advanced Facilities</div>
                </div>
                <button class="btn btn-lg btn-accent mx-auto lg:mx-0">Learn more</button>
            </div>
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

            sr.reveal('.departments', {interval: 200});
            sr.reveal('.departments_container', {interval: 200});
            
            });
        }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
