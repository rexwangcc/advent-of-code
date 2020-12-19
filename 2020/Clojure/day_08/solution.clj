(ns day_08.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "08")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(destruct
            [line]
            (let [[operation argument] (str/split line #" ")]
              [operation (read-string argument)]))]
    (->> file
         slurp
         str/split-lines
         (map destruct))))

(defn boot
  "Run all instructions until repetition. Use `mapv` since we need to index the
   index so cannot use lazy-sequence."
  [inputs]
  (letfn [(dispatch [[operation argument]]
            (case operation
              "jmp" [argument 0]
              "nop" [1 0]
              "acc" [1 argument]))
          (标注 [m] (zipmap (keys m) (repeat true)))]
    (let [inputs->map (mapv (fn [instruction] {instruction false}) inputs)]
      (loop [inputs->map inputs->map
             idx 0
             accumulator 0]
        (if (first (vals (get inputs->map idx)))
          ;; second round detected
          accumulator
          ;; still the first round
          (let [k (first (keys (get inputs->map idx)))
                [Δidx Δaccu] (dispatch k)]
            (recur (update-in inputs->map [idx] 标注)
                   (+ idx Δidx)
                   (+ accumulator Δaccu))))))))

(defn boot-cond
  "Run all instructions towards the end or repitition."
  [inputs]
  (letfn [(dispatch [[operation argument]]
            (case operation
              "jmp" [argument 0]
              "nop" [1 0]
              "acc" [1 argument]))
          (标注 [m] (zipmap (keys m) (repeat true)))]
    (let [inputs->map (mapv (fn [instruction] {instruction false}) inputs)]
      (loop [inputs->map inputs->map
             idx 0
             accumulator 0]
        (cond
          ;; terminates, returns the result
          (>= idx (count inputs->map)) accumulator
          ;; second round detected, bad!
          (first (vals (get inputs->map idx))) false
          ;; keep running
          :else (let [k (first (keys (get inputs->map idx)))
                      [Δidx Δaccu] (dispatch k)]
                  (recur (update-in inputs->map [idx] 标注)
                         (+ idx Δidx)
                         (+ accumulator Δaccu))))))))

(defn detect-and-fix
  "Brute-forcely detect all of jmp and nop operations
   by outsourcing executions to boot.
   Gotchas:
   - should use `nth` instead of `get/get-in` on seq
   - `update-in` expects vec not seq"
  [inputs]
  (letfn [(修复 [[ops arg]]
            (case ops
              "acc" ["acc" arg]
              "nop" ["jmp" arg]
              "jmp" ["nop" arg]))
          (可修复? [ops] (#{"nop" "jmp"} ops))]
    (for [[ops _] inputs
          idx (range (count inputs))
          :when (可修复? ops)
          :let [fixed (update-in (vec inputs) [idx] 修复)
                result (boot-cond fixed)]
          #_#_:while (false? result)]
      result)))

(defn part1
  [_]
  (->> "./day_08/inputs.txt"
       get-lines
       boot))

(defn part2
  [_]
  (->> "./day_08/inputs.txt"
       get-lines
       detect-and-fix
       (filter int?)
       first))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
