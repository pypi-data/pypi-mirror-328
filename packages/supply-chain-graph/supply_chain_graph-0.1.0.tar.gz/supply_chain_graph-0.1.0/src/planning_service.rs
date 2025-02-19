use crate::plan_proposal::ProposalStack;
use crate::specification::Specification;
use chrono::NaiveDate;
use crate::motivator::Motivator;
use std::fmt::Debug;

pub trait PlanningService: Debug {
    fn ask_internal(&self) -> String;
    fn ask(&self, quantity: f64, ask_date: NaiveDate, proposals: &mut ProposalStack, specification: &mut Specification, motivator: &mut Motivator) -> f64;
} 

