<template>
    <section class="appointem section">
        <div class="container mx-auto">
        <!-- TITLE -->
        <h2 class="appointment_title h2 mb-5 lg:mb-[50px] text-center lg:text-left">
            Book Appointment or call:
            <span class="text-accent-tertiary">(+51) 43 249 01</span>
        </h2>
        <!-- FORM -->
        <form class="appointment_form flex flex-col gap-y-5">
            <!-- SELECT -->
            <div class="flex flex-col lg:flex-row gap-5">
            <!-- SELECT1 -->
            <div class="select relative flex items-center">
                <!-- ICON -->
                <div class="absolute right-4">
                <i class="ri-arrow-down-s-line text-[26px] text-primary"></i>
                </div>
                <!-- SELECT -->
                <select class="appearance-none outline-none w-full px-4 bg-transparent">
                <option value="1">Select department</option>
                <option value="2">Department 1</option>
                <option value="3">Department 2</option>
                <option value="4">Department 3</option>
                </select>
            </div>
            <!-- SELECT2 -->
            <div class="select relative flex items-center">
                <!-- ICON -->
                <div class="absolute right-4">
                <i class="ri-arrow-down-s-line text-[26px] text-primary"></i>
                </div>
                <!-- SELECT -->
                <select class="appearance-none outline-none w-full px-4 bg-transparent">
                <option value="1">Select doctor</option>
                <option value="2">Dr. Jane Doe</option>
                <option value="3">Dr. Jhon Doe</option>
                <option value="4">Dr. Bob Smith</option>
                </select>
            </div>
            </div>
            <!-- INPUT -->
            <div class="flex flex-col lg:flex-row gap-5">
            <input type="text" class="input" placeholder="Full Name">
            <input type="text" class="input" placeholder="Phone Number">
            </div>
            <!-- INPUT -->
            <div class="flex flex-col lg:flex-row gap-5">
            <input type="date" class="input" placeholder="Full Name">
            <input type="time" class="input" placeholder="Phone Number">
            </div>
            <!-- BUTTON -->
            <button class="btn btn-lg btn-accent self-start" type="submit">Book an appointment</button>
        </form>
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

            sr.reveal('.appointment_title', {interval: 200});
            sr.reveal('.appointment_form', {interval: 200});
            });
        }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
