use std::sync::atomic::AtomicU32;
use std::sync::atomic::Ordering::SeqCst;

static COUNTER: AtomicU32 = AtomicU32::new(1);

pub struct UniqueId;
impl UniqueId {
    /// Returns a new unique u64 number each time it's called
    pub fn next() -> u32 {
        COUNTER.fetch_add(1, SeqCst)
    }
    /// Returns the current counter value without incrementing
    pub fn current() -> u32 {
        COUNTER.load(SeqCst)
    }
}

pub fn generate_unique_id() -> u32 {
    UniqueId::next()
}